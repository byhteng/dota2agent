# OpenDota Team Event Bundle

## Purpose

Use `scripts/download_opendota_team_event_bundle.py` to save a reusable raw data bundle for one team within one OpenDota league/event.

The bundle includes:

- `team_info.json`
- `league_info.json`
- `league_teams.json`
- `league_matches.json`
- `team_matches_in_league.json`
- `match_details/*.json`
- `match_details_manifest.json`
- `match_quality_report.json`
- `_summary.json`

## Output Path

Raw files are saved under:

`data/raw/opendota/{event_slug}/{team_slug}_{team_id}/{run_timestamp}/`

This keeps runs append-only and avoids overwriting older raw snapshots.

## Example

```bash
python3 scripts/download_opendota_team_event_bundle.py \
  --team-id 8291895 \
  --league-id 19422 \
  --slug esl_one_birmingham_2026 \
  --team-slug tundra_esports
```

## 2026-04-07 Example Result

- Data source: OpenDota API
- Team: `Tundra Esports` (`team_id=8291895`)
- Event: `ESL One Birmingham 2026` (`league_id=19422`)
- Sample size: `23` team matches in league, `23` match detail files
- Time range (UTC): `2026-03-22T11:59:56+00:00` to `2026-03-29T19:34:20+00:00`
- Raw bundle path:
  `data/raw/opendota/esl_one_birmingham_2026/tundra_esports_8291895/20260407_165109/`

## Notes

- Team inclusion is based on `/teams/{team_id}/matches` rows whose `leagueid` matches the requested `league_id`.
- This workflow targets one main event `league_id`; qualifiers or side events should be downloaded separately if needed.
- Match detail richness depends on OpenDota replay parsing coverage.
