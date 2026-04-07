#!/usr/bin/env python3
"""
Build a reusable OpenDota raw bundle for one team within one event/league.

This script references helpers from `opendota_download.py` and saves:
- league metadata
- league teams
- league matches
- team metadata
- team matches filtered to the target league
- full match detail JSON for each team match
- a small machine-readable summary

Example:
  python3 scripts/download_opendota_team_event_bundle.py \
    --team-id 8291895 \
    --league-id 19422 \
    --slug esl_one_birmingham_2026 \
    --team-slug tundra_esports
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from opendota_download import (
    RAW_ROOT,
    cleanup_empty_dir,
    fetch_match_details,
    get_json,
    save_json,
    summarize_match_detail,
)


def utc_iso(ts: int | None) -> str | None:
    if ts is None:
        return None
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def build_output_dir(args: argparse.Namespace) -> Path:
    run_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return (
        Path.cwd()
        / RAW_ROOT
        / "opendota"
        / args.slug
        / f"{args.team_slug}_{args.team_id}"
        / run_stamp
    )


def collect_team_league_matches(team_id: int, league_id: int, timeout: int, retries: int) -> tuple[list[dict[str, Any]], str]:
    matches, url = get_json(f"/teams/{team_id}/matches", timeout=timeout, retries=retries)
    if not isinstance(matches, list):
        raise RuntimeError(f"Unexpected response for /teams/{{team_id}}/matches: {type(matches)}")
    filtered = [m for m in matches if m.get("leagueid") == league_id]
    return filtered, url


def fetch_json_to_file(path: str, out_file: Path, timeout: int, retries: int) -> tuple[Any, str]:
    data, url = get_json(path, timeout=timeout, retries=retries)
    save_json(out_file, data)
    return data, url


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_summary(
    args: argparse.Namespace,
    team_info: Dict[str, Any],
    league_info: Any,
    league_teams: Any,
    league_matches: Any,
    team_league_matches: List[Dict[str, Any]],
    details_manifest: List[Dict[str, Any]],
    source_urls: Dict[str, str],
) -> Dict[str, Any]:
    opponents = Counter(m.get("opposing_team_name", "UNKNOWN") for m in team_league_matches)
    detail_quality = [item["quality"] for item in details_manifest if item.get("quality")]

    return {
        "data_source": "OpenDota API",
        "generated_at_local": datetime.now().isoformat(timespec="seconds"),
        "team_id": args.team_id,
        "team_name": team_info.get("name"),
        "league_id": args.league_id,
        "league_name": (
            league_info[0].get("name")
            if isinstance(league_info, list) and league_info
            else league_info.get("name")
            if isinstance(league_info, dict)
            else None
        ),
        "sample_size": {
            "team_matches_in_league": len(team_league_matches),
            "match_details_saved": len(details_manifest),
            "league_team_records": len(league_teams) if isinstance(league_teams, list) else None,
            "league_match_records": len(league_matches) if isinstance(league_matches, list) else None,
        },
        "assumptions": [
            "Team match inclusion is determined by OpenDota /teams/{team_id}/matches rows whose leagueid equals the requested league_id.",
            "Saved match detail JSON is whatever OpenDota /matches/{match_id} returned at download time.",
            "This bundle targets the main event league_id provided by the caller and does not automatically include separate qualifier leagues.",
        ],
        "limitations": [
            "OpenDota coverage depends on replay parsing and upstream data completeness.",
            "Some league endpoints may omit fields or differ in shape across tournaments.",
            "Match detail richness varies by parsed replay availability.",
        ],
        "time_range_utc": {
            "start": utc_iso(min((m.get("start_time") for m in team_league_matches), default=None)),
            "end": utc_iso(max((m.get("start_time") for m in team_league_matches), default=None)),
        },
        "opponents": dict(opponents),
        "source_urls": source_urls,
        "detail_quality_preview": detail_quality[:5],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Download a reusable OpenDota raw bundle for one team in one event.")
    parser.add_argument("--team-id", type=int, required=True, help="OpenDota team_id.")
    parser.add_argument("--league-id", type=int, required=True, help="OpenDota league_id.")
    parser.add_argument("--slug", type=str, required=True, help="Tournament slug used in the output path.")
    parser.add_argument("--team-slug", type=str, required=True, help="Team slug used in the output path.")
    parser.add_argument("--delay", type=float, default=1.1, help="Seconds to wait between match detail requests.")
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout in seconds.")
    parser.add_argument("--retries", type=int, default=3, help="Retry count for transient HTTP errors.")
    parser.add_argument("--skip-existing", action="store_true", help="Reuse match detail files that already exist in this run directory.")
    args = parser.parse_args()

    out_dir = build_output_dir(args)
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        team_info, team_url = fetch_json_to_file(
            f"/teams/{args.team_id}",
            out_dir / "team_info.json",
            timeout=args.timeout,
            retries=args.retries,
        )
        league_info, league_url = fetch_json_to_file(
            f"/leagues/{args.league_id}",
            out_dir / "league_info.json",
            timeout=args.timeout,
            retries=args.retries,
        )
        league_teams, league_teams_url = fetch_json_to_file(
            f"/leagues/{args.league_id}/teams",
            out_dir / "league_teams.json",
            timeout=args.timeout,
            retries=args.retries,
        )
        league_matches, league_matches_url = fetch_json_to_file(
            f"/leagues/{args.league_id}/matches",
            out_dir / "league_matches.json",
            timeout=args.timeout,
            retries=args.retries,
        )

        team_league_matches, team_matches_url = collect_team_league_matches(
            args.team_id,
            args.league_id,
            timeout=args.timeout,
            retries=args.retries,
        )
        save_json(out_dir / "team_matches_in_league.json", team_league_matches)

        details_manifest = fetch_match_details(
            team_league_matches,
            out_dir,
            delay=args.delay,
            skip_existing=args.skip_existing,
            timeout=args.timeout,
            retries=args.retries,
        )
        save_json(out_dir / "match_details_manifest.json", details_manifest)
        save_json(
            out_dir / "match_quality_report.json",
            [summarize_match_detail(load_json(path)) for path in sorted((out_dir / "match_details").glob("*.json"))],
        )

        source_urls = {
            "team": team_url,
            "league": league_url,
            "league_teams": league_teams_url,
            "league_matches": league_matches_url,
            "team_matches": team_matches_url,
        }
        save_json(
            out_dir / "_summary.json",
            build_summary(
                args=args,
                team_info=team_info if isinstance(team_info, dict) else {},
                league_info=league_info,
                league_teams=league_teams,
                league_matches=league_matches,
                team_league_matches=team_league_matches,
                details_manifest=details_manifest,
                source_urls=source_urls,
            ),
        )
    except Exception:
        cleanup_empty_dir(out_dir, stop_at=Path.cwd() / RAW_ROOT)
        raise

    print(f"Saved event bundle to: {out_dir}")
    print(f"- Team league matches: {len(team_league_matches)}")
    print(f"- Match details: {len(details_manifest)}")
    print("Example run:")
    print(
        "python3 scripts/download_opendota_team_event_bundle.py "
        f"--team-id {args.team_id} --league-id {args.league_id} "
        f"--slug {args.slug} --team-slug {args.team_slug}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
