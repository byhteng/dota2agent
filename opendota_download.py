#!/usr/bin/env python3
"""
OpenDota downloader (stdlib-only)

Examples:
  python opendota_download.py teams --name tundra --limit 5
  python opendota_download.py team-matches --team-id 8291895 --league-id 19422 --limit 10
  python opendota_download.py team-matches --team-id 8291895 --start-date 2026-03-01 --end-date 2026-03-31
  python opendota_download.py team-dataset --team-id 8291895 --league-id 19422 --limit 5
  python opendota_download.py team-dataset --team-id 8291895 --start-date 2026-03-01 --end-date 2026-03-31 --skip-existing
  python opendota_download.py pro-matches --limit 20 --fetch-details
  python opendota_download.py match --match-id 8228136473

Optional:
  export OPENDOTA_API_KEY=your_key_here
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE_URL = "https://api.opendota.com/api"
RAW_ROOT = Path("data/raw")
DEFAULT_DELAY = 1.1
DEFAULT_TIMEOUT = 30


def now_str() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def default_output_root() -> Path:
    return Path.cwd() / RAW_ROOT


def make_output_dir(output_dir: str | None, prefix: str = "opendota_dump") -> Path:
    if output_dir:
        out = Path(output_dir)
    else:
        out = default_output_root() / f"{prefix}_{now_str()}"
    out.mkdir(parents=True, exist_ok=True)
    return out


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def build_url(path: str, params: Dict[str, Any] | None = None) -> str:
    params = dict(params or {})
    api_key = os.getenv("OPENDOTA_API_KEY")
    if api_key:
        params["api_key"] = api_key
    query = urlencode({k: v for k, v in params.items() if v is not None})
    return f"{BASE_URL}{path}" + (f"?{query}" if query else "")


def get_json(
    path: str,
    params: Dict[str, Any] | None = None,
    timeout: int = DEFAULT_TIMEOUT,
    retries: int = 3,
    retry_wait: float = 2.0,
) -> Tuple[Any, str]:
    url = build_url(path, params)
    req = Request(
        url,
        headers={
            "User-Agent": "opendota-downloader/0.2",
            "Accept": "application/json",
        },
    )

    for attempt in range(1, retries + 1):
        try:
            with urlopen(req, timeout=timeout) as resp:
                body = resp.read().decode("utf-8")
                return json.loads(body), url
        except HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")
            if e.code in {429, 500, 502, 503, 504} and attempt < retries:
                time.sleep(retry_wait * attempt)
                continue
            raise RuntimeError(f"HTTP {e.code} for {url}\n{detail}") from e
        except URLError as e:
            if attempt < retries:
                time.sleep(retry_wait * attempt)
                continue
            raise RuntimeError(f"Network error for {url}: {e}") from e
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Invalid JSON from {url}: {e}") from e

    raise RuntimeError(f"Failed to fetch {url}")


def parse_ymd(value: str | None, name: str) -> int | None:
    if value is None:
        return None
    try:
        dt = datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"{name} must be YYYY-MM-DD") from e
    return int(dt.timestamp())


def build_match_filters(args: argparse.Namespace) -> Dict[str, Any]:
    start_ts = parse_ymd(getattr(args, "start_date", None), "--start-date")
    end_ts = parse_ymd(getattr(args, "end_date", None), "--end-date")
    if start_ts is not None and end_ts is not None and start_ts > end_ts:
        raise RuntimeError("--start-date must be on or before --end-date")

    return {
        "league_id": getattr(args, "league_id", None),
        "start_ts": start_ts,
        "end_ts": end_ts,
    }


def filter_team_matches(matches: List[Dict[str, Any]], filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    league_id = filters["league_id"]
    start_ts = filters["start_ts"]
    end_ts = filters["end_ts"]
    filtered = []

    for match in matches:
        match_start = match.get("start_time")
        match_league = match.get("leagueid")
        if league_id is not None and match_league != league_id:
            continue
        if start_ts is not None and (match_start is None or match_start < start_ts):
            continue
        if end_ts is not None and match_start is not None and match_start >= end_ts + 86400:
            continue
        filtered.append(match)

    return filtered


def slice_matches(matches: List[Dict[str, Any]], limit: int | None) -> List[Dict[str, Any]]:
    if limit is None:
        return matches
    return matches[:limit]


def summarize_match_detail(data: Dict[str, Any]) -> Dict[str, Any]:
    players = data.get("players") or []
    has_picks_bans = bool(data.get("picks_bans"))
    has_objectives = bool(data.get("objectives"))
    has_teamfights = bool(data.get("teamfights"))
    has_radiant_gold_adv = bool(data.get("radiant_gold_adv"))
    has_radiant_xp_adv = bool(data.get("radiant_xp_adv"))
    has_cosmetics = bool(data.get("cosmetics"))

    player_flags = {
        "obs_log_players": 0,
        "sen_log_players": 0,
        "purchase_log_players": 0,
        "item_usage_players": 0,
        "killed_players": 0,
        "buyback_log_players": 0,
    }
    for player in players:
        if player.get("obs_log"):
            player_flags["obs_log_players"] += 1
        if player.get("sen_log"):
            player_flags["sen_log_players"] += 1
        if player.get("purchase_log"):
            player_flags["purchase_log_players"] += 1
        if player.get("item_usage"):
            player_flags["item_usage_players"] += 1
        if player.get("killed"):
            player_flags["killed_players"] += 1
        if player.get("buyback_log"):
            player_flags["buyback_log_players"] += 1

    return {
        "match_id": data.get("match_id"),
        "radiant_win": data.get("radiant_win"),
        "start_time": data.get("start_time"),
        "duration": data.get("duration"),
        "leagueid": data.get("leagueid"),
        "has_picks_bans": has_picks_bans,
        "has_objectives": has_objectives,
        "has_teamfights": has_teamfights,
        "has_radiant_gold_adv": has_radiant_gold_adv,
        "has_radiant_xp_adv": has_radiant_xp_adv,
        "has_cosmetics": has_cosmetics,
        "player_count": len(players),
        **player_flags,
    }


def fetch_match_details(
    matches: List[Dict[str, Any]],
    out_dir: Path,
    delay: float,
    skip_existing: bool,
    timeout: int,
    retries: int,
) -> List[Dict[str, Any]]:
    details_dir = out_dir / "match_details"
    details_dir.mkdir(parents=True, exist_ok=True)
    manifest: List[Dict[str, Any]] = []

    for idx, m in enumerate(matches, start=1):
        match_id = m.get("match_id")
        if match_id is None:
            print(f"[skip] missing match_id in item #{idx}", file=sys.stderr)
            continue

        file_path = details_dir / f"{match_id}.json"
        if skip_existing and file_path.exists():
            try:
                with file_path.open("r", encoding="utf-8") as f:
                    existing = json.load(f)
            except json.JSONDecodeError:
                existing = {"match_id": match_id}
            manifest.append(
                {
                    "match_id": match_id,
                    "file": file_path.name,
                    "source_url": build_url(f"/matches/{match_id}"),
                    "status": "skipped_existing",
                    "quality": summarize_match_detail(existing),
                }
            )
            print(f"[{idx}/{len(matches)}] reused existing match {match_id} -> {file_path}")
            continue

        data, url = get_json(f"/matches/{match_id}", timeout=timeout, retries=retries)
        save_json(file_path, data)
        manifest.append(
            {
                "match_id": match_id,
                "file": file_path.name,
                "source_url": url,
                "status": "downloaded",
                "quality": summarize_match_detail(data),
            }
        )
        print(f"[{idx}/{len(matches)}] saved match {match_id} -> {file_path}")
        if idx < len(matches):
            time.sleep(delay)

    return manifest


def write_summary_meta(
    out: Path,
    source_url: str,
    count: int,
    command: str,
    args: argparse.Namespace,
    filters: Dict[str, Any] | None = None,
) -> None:
    meta = {
        "source_url": source_url,
        "command": command,
        "count": count,
        "team_id": getattr(args, "team_id", None),
        "league_id": getattr(args, "league_id", None),
        "start_date": getattr(args, "start_date", None),
        "end_date": getattr(args, "end_date", None),
        "limit": getattr(args, "limit", None),
        "generated_at_local": datetime.now().isoformat(timespec="seconds"),
    }
    if filters:
        meta["filters"] = filters
    save_json(out / "_meta.json", meta)


def cmd_teams(args: argparse.Namespace) -> None:
    out = make_output_dir(args.output_dir, prefix="opendota_teams")
    teams, url = get_json("/teams", timeout=args.timeout, retries=args.retries)
    if not isinstance(teams, list):
        raise RuntimeError(f"Unexpected response for /teams: {type(teams)}")

    if args.name:
        q = args.name.lower()
        teams = [t for t in teams if q in str(t.get("name", "")).lower()]

    if args.limit:
        teams = teams[: args.limit]

    save_json(out / "teams.json", teams)
    write_summary_meta(out, url, len(teams), "teams", args)

    print(f"Saved {len(teams)} teams to: {out / 'teams.json'}")
    if teams:
        print("\nTop teams by filter:")
        for t in teams[:10]:
            print(f"- team_id={t.get('team_id')}  name={t.get('name')}")


def cmd_team_matches(args: argparse.Namespace) -> None:
    out = make_output_dir(args.output_dir, prefix=f"opendota_team_{args.team_id}_matches")
    matches, url = get_json(f"/teams/{args.team_id}/matches", timeout=args.timeout, retries=args.retries)
    if not isinstance(matches, list):
        raise RuntimeError(f"Unexpected response for /teams/{{team_id}}/matches: {type(matches)}")

    filters = build_match_filters(args)
    raw_count = len(matches)
    matches = filter_team_matches(matches, filters)
    matches = slice_matches(matches, args.limit)

    save_json(out / f"team_{args.team_id}_matches.json", matches)
    write_summary_meta(out, url, len(matches), "team-matches", args, filters=filters | {"raw_count": raw_count})
    print(f"Saved {len(matches)} filtered team matches to: {out / f'team_{args.team_id}_matches.json'}")

    if args.fetch_details:
        manifest = fetch_match_details(
            matches,
            out,
            delay=args.delay,
            skip_existing=args.skip_existing,
            timeout=args.timeout,
            retries=args.retries,
        )
        save_json(out / "match_details_manifest.json", manifest)


def cmd_team_dataset(args: argparse.Namespace) -> None:
    out = make_output_dir(args.output_dir, prefix=f"opendota_team_{args.team_id}_dataset")
    matches, url = get_json(f"/teams/{args.team_id}/matches", timeout=args.timeout, retries=args.retries)
    if not isinstance(matches, list):
        raise RuntimeError(f"Unexpected response for /teams/{{team_id}}/matches: {type(matches)}")

    filters = build_match_filters(args)
    raw_count = len(matches)
    filtered_matches = filter_team_matches(matches, filters)
    filtered_matches = slice_matches(filtered_matches, args.limit)
    save_json(out / f"team_{args.team_id}_matches.json", filtered_matches)

    manifest = fetch_match_details(
        filtered_matches,
        out,
        delay=args.delay,
        skip_existing=args.skip_existing,
        timeout=args.timeout,
        retries=args.retries,
    )
    quality_report = [item["quality"] for item in manifest]

    save_json(out / "match_details_manifest.json", manifest)
    save_json(out / "match_quality_report.json", quality_report)
    write_summary_meta(
        out,
        url,
        len(filtered_matches),
        "team-dataset",
        args,
        filters=filters | {"raw_count": raw_count},
    )

    print(f"Saved dataset with {len(filtered_matches)} matches to: {out}")
    print(f"Match list: {out / f'team_{args.team_id}_matches.json'}")
    print(f"Details manifest: {out / 'match_details_manifest.json'}")
    print(f"Quality report: {out / 'match_quality_report.json'}")


def cmd_pro_matches(args: argparse.Namespace) -> None:
    out = make_output_dir(args.output_dir, prefix="opendota_pro_matches")
    params = {}
    if args.less_than_match_id is not None:
        params["less_than_match_id"] = args.less_than_match_id

    matches, url = get_json("/proMatches", params=params, timeout=args.timeout, retries=args.retries)
    if not isinstance(matches, list):
        raise RuntimeError(f"Unexpected response for /proMatches: {type(matches)}")

    matches = slice_matches(matches, args.limit)
    save_json(out / "pro_matches.json", matches)
    write_summary_meta(out, url, len(matches), "pro-matches", args)
    print(f"Saved {len(matches)} pro matches to: {out / 'pro_matches.json'}")

    if args.fetch_details:
        manifest = fetch_match_details(
            matches,
            out,
            delay=args.delay,
            skip_existing=args.skip_existing,
            timeout=args.timeout,
            retries=args.retries,
        )
        save_json(out / "match_details_manifest.json", manifest)


def cmd_match(args: argparse.Namespace) -> None:
    out = make_output_dir(args.output_dir, prefix=f"opendota_match_{args.match_id}")
    match, url = get_json(f"/matches/{args.match_id}", timeout=args.timeout, retries=args.retries)
    save_json(out / f"match_{args.match_id}.json", match)
    write_summary_meta(out, url, 1, "match", args)
    print(f"Saved match details to: {out / f'match_{args.match_id}.json'}")


def add_common_request_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--output-dir", type=str, default=None, help="Directory to write JSON files into.")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="HTTP timeout in seconds.")
    parser.add_argument("--retries", type=int, default=3, help="Retry count for transient HTTP errors.")


def add_detail_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY, help="Seconds to wait between detail requests.")
    parser.add_argument("--skip-existing", action="store_true", help="Do not overwrite an existing match detail file.")


def add_match_filter_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--league-id", type=int, default=None, help="Keep only matches from one league/tournament.")
    parser.add_argument("--start-date", type=str, default=None, help="Keep matches on/after YYYY-MM-DD (UTC).")
    parser.add_argument("--end-date", type=str, default=None, help="Keep matches on/before YYYY-MM-DD (UTC).")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Download data from the OpenDota API.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_teams = sub.add_parser("teams", help="Download the team list and optionally filter by name.")
    p_teams.add_argument("--name", type=str, default=None, help="Case-insensitive substring match on team name.")
    p_teams.add_argument("--limit", type=int, default=20, help="Keep only the first N teams after filtering.")
    add_common_request_args(p_teams)
    p_teams.set_defaults(func=cmd_teams)

    p_team_matches = sub.add_parser("team-matches", help="Download match list for a team and filter it locally.")
    p_team_matches.add_argument("--team-id", type=int, required=True, help="OpenDota team_id.")
    p_team_matches.add_argument("--limit", type=int, default=20, help="Keep only the first N matches after filtering.")
    p_team_matches.add_argument("--fetch-details", action="store_true", help="Also fetch /matches/{match_id} for each listed match.")
    add_match_filter_args(p_team_matches)
    add_common_request_args(p_team_matches)
    add_detail_args(p_team_matches)
    p_team_matches.set_defaults(func=cmd_team_matches)

    p_dataset = sub.add_parser(
        "team-dataset",
        help="Build a reusable raw dataset for one team by saving the match list, full match details, and a quality report.",
    )
    p_dataset.add_argument("--team-id", type=int, required=True, help="OpenDota team_id.")
    p_dataset.add_argument("--limit", type=int, default=10, help="Keep only the first N matches after filtering.")
    add_match_filter_args(p_dataset)
    add_common_request_args(p_dataset)
    add_detail_args(p_dataset)
    p_dataset.set_defaults(func=cmd_team_dataset)

    p_pro = sub.add_parser("pro-matches", help="Download recent pro matches.")
    p_pro.add_argument("--limit", type=int, default=20, help="Keep only the first N matches.")
    p_pro.add_argument("--less-than-match-id", type=int, default=None, help="Pass less_than_match_id to /proMatches.")
    p_pro.add_argument("--fetch-details", action="store_true", help="Also fetch /matches/{match_id} for each listed match.")
    add_common_request_args(p_pro)
    add_detail_args(p_pro)
    p_pro.set_defaults(func=cmd_pro_matches)

    p_match = sub.add_parser("match", help="Download one match's full detail JSON.")
    p_match.add_argument("--match-id", type=int, required=True, help="Match ID.")
    add_common_request_args(p_match)
    p_match.set_defaults(func=cmd_match)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        args.func(args)
        return 0
    except KeyboardInterrupt:
        print("Interrupted.", file=sys.stderr)
        return 130
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
