# OpenDota API Local Docs

## Snapshot

- Source: `https://api.opendota.com/api`
- Generated at (UTC): `2026-04-07T08:22:52.448646+00:00`
- OpenAPI version: `3.0.3`
- API title: `OpenDota API`
- API version: `31.1.0`
- Base server: `https://api.opendota.com/api`
- Paths: `55`
- Operations: `55`
- Tags: `25`
- Raw spec snapshot: `data/raw/opendota_docs/openapi_20260407_082252.json`
- Endpoint CSV: `data/processed/opendota_docs/endpoints_20260407_082252.csv`
- Endpoint JSON: `data/processed/opendota_docs/endpoints_20260407_082252.json`

## Official Description

# Introduction
The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays.

You can find data that can be used to convert hero and ability IDs and other information provided by the API from the [dotaconstants](https://github.com/odota/dotaconstants) repository.

You can use the API without a key, but registering for a key allows increased rate limits and usage. Check out the [API page](https://www.opendota.com/api-keys) to learn more.

## Tags

- [benchmarks](#benchmarks) (1)
- [constants](#constants) (1)
- [distributions](#distributions) (1)
- [explorer](#explorer) (1)
- [findMatches](#findmatches) (1)
- [health](#health) (1)
- [hero stats](#hero-stats) (1)
- [heroes](#heroes) (6)
- [leagues](#leagues) (5)
- [live](#live) (1)
- [matches](#matches) (1)
- [metadata](#metadata) (1)
- [parsed matches](#parsed-matches) (1)
- [players](#players) (15)
- [pro matches](#pro-matches) (1)
- [pro players](#pro-players) (1)
- [public matches](#public-matches) (1)
- [rankings](#rankings) (1)
- [records](#records) (1)
- [request](#request) (2)
- [scenarios](#scenarios) (3)
- [schema](#schema) (1)
- [search](#search) (1)
- [teams](#teams) (5)
- [top players](#top-players) (1)

## Endpoint Index

| Method | Path | Tag | Summary |
| --- | --- | --- | --- |
| `GET` | `/benchmarks` | `benchmarks` | GET /benchmarks |
| `GET` | `/constants/{resource}` | `constants` | GET /constants |
| `GET` | `/distributions` | `distributions` | GET /distributions |
| `GET` | `/explorer` | `explorer` | GET /explorer |
| `GET` | `/findMatches` | `findMatches` | GET / |
| `GET` | `/health` | `health` | GET /health |
| `GET` | `/heroStats` | `hero stats` | GET /heroStats |
| `GET` | `/heroes` | `heroes` | GET /heroes |
| `GET` | `/heroes/{hero_id}/durations` | `heroes` | GET /heroes/{hero_id}/durations |
| `GET` | `/heroes/{hero_id}/itemPopularity` | `heroes` | GET /heroes/{hero_id}/itemPopularity |
| `GET` | `/heroes/{hero_id}/matches` | `heroes` | GET /heroes/{hero_id}/matches |
| `GET` | `/heroes/{hero_id}/matchups` | `heroes` | GET /heroes/{hero_id}/matchups |
| `GET` | `/heroes/{hero_id}/players` | `heroes` | GET /heroes/{hero_id}/players |
| `GET` | `/leagues` | `leagues` | GET /leagues |
| `GET` | `/leagues/{league_id}` | `leagues` | GET /leagues/{league_id} |
| `GET` | `/leagues/{league_id}/matchIds` | `leagues` | GET /leagues/{league_id}/matchIds |
| `GET` | `/leagues/{league_id}/matches` | `leagues` | GET /leagues/{league_id}/matches |
| `GET` | `/leagues/{league_id}/teams` | `leagues` | GET /leagues/{league_id}/teams |
| `GET` | `/live` | `live` | GET /live |
| `GET` | `/matches/{match_id}` | `matches` | GET /matches/{match_id} |
| `GET` | `/metadata` | `metadata` | GET /metadata |
| `GET` | `/parsedMatches` | `parsed matches` | GET /parsedMatches |
| `GET` | `/players/{account_id}` | `players` | GET /players/{account_id} |
| `GET` | `/players/{account_id}/counts` | `players` | GET /players/{account_id}/counts |
| `GET` | `/players/{account_id}/heroes` | `players` | GET /players/{account_id}/heroes |
| `GET` | `/players/{account_id}/histograms/{field}` | `players` | GET /players/{account_id}/histograms |
| `GET` | `/players/{account_id}/matches` | `players` | GET /players/{account_id}/matches |
| `GET` | `/players/{account_id}/peers` | `players` | GET /players/{account_id}/peers |
| `GET` | `/players/{account_id}/pros` | `players` | GET /players/{account_id}/pros |
| `GET` | `/players/{account_id}/rankings` | `players` | GET /players/{account_id}/rankings |
| `GET` | `/players/{account_id}/ratings` | `players` | GET /players/{account_id}/ratings |
| `GET` | `/players/{account_id}/recentMatches` | `players` | GET /players/{account_id}/recentMatches |
| `POST` | `/players/{account_id}/refresh` | `players` | POST /players/{account_id}/refresh |
| `GET` | `/players/{account_id}/totals` | `players` | GET /players/{account_id}/totals |
| `GET` | `/players/{account_id}/wardmap` | `players` | GET /players/{account_id}/wardmap |
| `GET` | `/players/{account_id}/wl` | `players` | GET /players/{account_id}/wl |
| `GET` | `/players/{account_id}/wordcloud` | `players` | GET /players/{account_id}/wordcloud |
| `GET` | `/proMatches` | `pro matches` | GET /proMatches |
| `GET` | `/proPlayers` | `pro players` | GET /proPlayers |
| `GET` | `/publicMatches` | `public matches` | GET /publicMatches |
| `GET` | `/rankings` | `rankings` | GET /rankings |
| `GET` | `/records/{field}` | `records` | GET /records/{field} |
| `GET` | `/request/{jobId}` | `request` | GET /request/{jobId} |
| `POST` | `/request/{match_id}` | `request` | POST /request/{match_id} |
| `GET` | `/scenarios/itemTimings` | `scenarios` | GET /scenarios/itemTimings |
| `GET` | `/scenarios/laneRoles` | `scenarios` | GET /scenarios/laneRoles |
| `GET` | `/scenarios/misc` | `scenarios` | GET /scenarios/misc |
| `GET` | `/schema` | `schema` | GET /schema |
| `GET` | `/search` | `search` | GET /search |
| `GET` | `/teams` | `teams` | GET /teams |
| `GET` | `/teams/{team_id}` | `teams` | GET /teams/{team_id} |
| `GET` | `/teams/{team_id}/heroes` | `teams` | GET /teams/{team_id}/heroes |
| `GET` | `/teams/{team_id}/matches` | `teams` | GET /teams/{team_id}/matches |
| `GET` | `/teams/{team_id}/players` | `teams` | GET /teams/{team_id}/players |
| `GET` | `/topPlayers` | `top players` | GET /topPlayers |

## benchmarks
<a id="benchmarks"></a>

### `GET /benchmarks`

- Summary: GET /benchmarks
- Description: Benchmarks of average stat values for a hero
- Operation ID: `get_benchmarks`
- Response codes: `200`
- Response schema: `200:BenchmarksResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `hero_id` | `query` | `yes` | `string` | Hero ID |

## constants
<a id="constants"></a>

### `GET /constants/{resource}`

- Summary: GET /constants
- Description: Get static game data mirrored from the dotaconstants repository.
- Operation ID: `get_constants_by_resource`
- Response codes: `200`
- Response schema: `200:oneOf`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `resource` | `path` | `yes` | `string` | Resource name e.g. `heroes`. [List of resources](https://github.com/odota/dotaconstants/tree/master/build) |

## distributions
<a id="distributions"></a>

### `GET /distributions`

- Summary: GET /distributions
- Description: Distributions of MMR data by bracket and country
- Operation ID: `get_distributions`
- Response codes: `200`
- Response schema: `200:DistributionsResponse`

No documented parameters.

## explorer
<a id="explorer"></a>

### `GET /explorer`

- Summary: GET /explorer
- Description: Submit arbitrary SQL queries to the database
- Operation ID: `get_explorer`
- Response codes: `200`
- Response schema: `200:object`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `sql` | `query` | `no` | `string` | The PostgreSQL query as percent-encoded string. |

## findMatches
<a id="findmatches"></a>

### `GET /findMatches`

- Summary: GET /
- Description: Finds recent matches by heroes played
- Operation ID: `get_find_matches`
- Response codes: `200`
- Response schema: `200:array[object]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `teamA` | `query` | `no` | `array[integer]` | Hero IDs on first team (array) |
| `teamB` | `query` | `no` | `array[integer]` | Hero IDs on second team (array) |

## health
<a id="health"></a>

### `GET /health`

- Summary: GET /health
- Description: Get service health data
- Operation ID: `get_health`
- Response codes: `200`
- Response schema: `200:object`

No documented parameters.

## hero stats
<a id="hero-stats"></a>

### `GET /heroStats`

- Summary: GET /heroStats
- Description: Get stats about hero performance in recent matches
- Operation ID: `get_hero_stats`
- Response codes: `200`
- Response schema: `200:array[HeroStatsResponse]`

No documented parameters.

## heroes
<a id="heroes"></a>

### `GET /heroes`

- Summary: GET /heroes
- Description: Get hero data
- Operation ID: `get_heroes`
- Response codes: `200`
- Response schema: `200:array[HeroObjectResponse]`

No documented parameters.

### `GET /heroes/{hero_id}/durations`

- Summary: GET /heroes/{hero_id}/durations
- Description: Get hero performance over a range of match durations
- Operation ID: `get_heroes_by_hero_id_select_durations`
- Response codes: `200`
- Response schema: `200:array[HeroDurationsResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `hero_id` | `path` | `yes` | `integer` | Hero ID |

### `GET /heroes/{hero_id}/itemPopularity`

- Summary: GET /heroes/{hero_id}/itemPopularity
- Description: Get item popularity of hero categoried by start, early, mid and late game, analyzed from professional games
- Operation ID: `get_heroes_by_hero_id_select_item_popularity`
- Response codes: `200`
- Response schema: `200:HeroItemPopularityResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `hero_id` | `path` | `yes` | `integer` | Hero ID |

### `GET /heroes/{hero_id}/matches`

- Summary: GET /heroes/{hero_id}/matches
- Description: Get recent matches with a hero
- Operation ID: `get_heroes_by_hero_id_select_matches`
- Response codes: `200`
- Response schema: `200:array[MatchObjectResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `hero_id` | `path` | `yes` | `integer` | Hero ID |

### `GET /heroes/{hero_id}/matchups`

- Summary: GET /heroes/{hero_id}/matchups
- Description: Get results against other heroes for a hero
- Operation ID: `get_heroes_by_hero_id_select_matchups`
- Response codes: `200`
- Response schema: `200:array[HeroMatchupsResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `hero_id` | `path` | `yes` | `integer` | Hero ID |

### `GET /heroes/{hero_id}/players`

- Summary: GET /heroes/{hero_id}/players
- Description: Get players who have played this hero
- Operation ID: `get_heroes_by_hero_id_select_players`
- Response codes: `200`
- Response schema: `200:array[array[PlayerObjectResponse]]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `hero_id` | `path` | `yes` | `integer` | Hero ID |

## leagues
<a id="leagues"></a>

### `GET /leagues`

- Summary: GET /leagues
- Description: Get league data
- Operation ID: `get_leagues`
- Response codes: `200`
- Response schema: `200:array[LeagueObjectResponse]`

No documented parameters.

### `GET /leagues/{league_id}`

- Summary: GET /leagues/{league_id}
- Description: Get data for a league
- Operation ID: `get_leagues_by_league_id`
- Response codes: `200`
- Response schema: `200:array[LeagueObjectResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `league_id` | `path` | `yes` | `integer` | League ID |

### `GET /leagues/{league_id}/matchIds`

- Summary: GET /leagues/{league_id}/matchIds
- Description: Get match IDs for a league (including amateur leagues)
- Operation ID: `get_leagues_by_league_id_select_match_ids`
- Response codes: `200`
- Response schema: `200:array[string]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `league_id` | `path` | `yes` | `integer` | League ID |

### `GET /leagues/{league_id}/matches`

- Summary: GET /leagues/{league_id}/matches
- Description: Get matches for a league (excluding amateur leagues)
- Operation ID: `get_leagues_by_league_id_select_matches`
- Response codes: `200`
- Response schema: `200:MatchObjectResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `league_id` | `path` | `yes` | `integer` | League ID |

### `GET /leagues/{league_id}/teams`

- Summary: GET /leagues/{league_id}/teams
- Description: Get teams for a league
- Operation ID: `get_leagues_by_league_id_select_teams`
- Response codes: `200`
- Response schema: `200:TeamObjectResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `league_id` | `path` | `yes` | `integer` | League ID |

## live
<a id="live"></a>

### `GET /live`

- Summary: GET /live
- Description: Get top currently ongoing live games
- Operation ID: `get_live`
- Response codes: `200`
- Response schema: `200:array[object]`

No documented parameters.

## matches
<a id="matches"></a>

### `GET /matches/{match_id}`

- Summary: GET /matches/{match_id}
- Description: Match data
- Operation ID: `get_matches_by_match_id`
- Response codes: `200`
- Response schema: `200:MatchResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `match_id` | `path` | `yes` | `integer` | - |

## metadata
<a id="metadata"></a>

### `GET /metadata`

- Summary: GET /metadata
- Description: Site metadata
- Operation ID: `get_metadata`
- Response codes: `200`
- Response schema: `200:MetadataResponse`

No documented parameters.

## parsed matches
<a id="parsed-matches"></a>

### `GET /parsedMatches`

- Summary: GET /parsedMatches
- Description: Get list of parsed match IDs
- Operation ID: `get_parsed_matches`
- Response codes: `200`
- Response schema: `200:array[ParsedMatchesResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `less_than_match_id` | `query` | `no` | `integer` | Get matches with a match ID lower than this value |

## players
<a id="players"></a>

### `GET /players/{account_id}`

- Summary: GET /players/{account_id}
- Description: Player data
- Operation ID: `get_players_by_account_id`
- Response codes: `200`
- Response schema: `200:PlayersResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |

### `GET /players/{account_id}/counts`

- Summary: GET /players/{account_id}/counts
- Description: Counts in categories
- Operation ID: `get_players_by_account_id_select_counts`
- Response codes: `200`
- Response schema: `200:PlayerCountsResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |
| `limit` | `query` | `no` | `integer` | Number of matches to limit to |
| `offset` | `query` | `no` | `integer` | Number of matches to offset start by |
| `win` | `query` | `no` | `integer` | Whether the player won |
| `patch` | `query` | `no` | `integer` | Patch ID, from dotaconstants |
| `game_mode` | `query` | `no` | `integer` | Game Mode ID |
| `lobby_type` | `query` | `no` | `integer` | Lobby type ID |
| `region` | `query` | `no` | `integer` | Region ID |
| `date` | `query` | `no` | `integer` | Days previous |
| `lane_role` | `query` | `no` | `integer` | Lane Role ID |
| `hero_id` | `query` | `no` | `integer` | Hero ID |
| `is_radiant` | `query` | `no` | `integer` | Whether the player was radiant |
| `included_account_id` | `query` | `no` | `integer` | Account IDs in the match (array) |
| `excluded_account_id` | `query` | `no` | `integer` | Account IDs not in the match (array) |
| `with_hero_id` | `query` | `no` | `integer` | Hero IDs on the player's team (array) |
| `against_hero_id` | `query` | `no` | `integer` | Hero IDs against the player's team (array) |
| `significant` | `query` | `no` | `integer` | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | `query` | `no` | `integer` | The minimum number of games played, for filtering hero stats |
| `sort` | `query` | `no` | `string` | The field to return matches sorted by in descending order |

### `GET /players/{account_id}/heroes`

- Summary: GET /players/{account_id}/heroes
- Description: Heroes played
- Operation ID: `get_players_by_account_id_select_heroes`
- Response codes: `200`
- Response schema: `200:array[PlayerHeroesResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |
| `limit` | `query` | `no` | `integer` | Number of matches to limit to |
| `offset` | `query` | `no` | `integer` | Number of matches to offset start by |
| `win` | `query` | `no` | `integer` | Whether the player won |
| `patch` | `query` | `no` | `integer` | Patch ID, from dotaconstants |
| `game_mode` | `query` | `no` | `integer` | Game Mode ID |
| `lobby_type` | `query` | `no` | `integer` | Lobby type ID |
| `region` | `query` | `no` | `integer` | Region ID |
| `date` | `query` | `no` | `integer` | Days previous |
| `lane_role` | `query` | `no` | `integer` | Lane Role ID |
| `hero_id` | `query` | `no` | `integer` | Hero ID |
| `is_radiant` | `query` | `no` | `integer` | Whether the player was radiant |
| `included_account_id` | `query` | `no` | `integer` | Account IDs in the match (array) |
| `excluded_account_id` | `query` | `no` | `integer` | Account IDs not in the match (array) |
| `with_hero_id` | `query` | `no` | `integer` | Hero IDs on the player's team (array) |
| `against_hero_id` | `query` | `no` | `integer` | Hero IDs against the player's team (array) |
| `significant` | `query` | `no` | `integer` | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | `query` | `no` | `integer` | The minimum number of games played, for filtering hero stats |
| `sort` | `query` | `no` | `string` | The field to return matches sorted by in descending order |

### `GET /players/{account_id}/histograms/{field}`

- Summary: GET /players/{account_id}/histograms
- Description: Distribution of matches in a single stat
- Operation ID: `get_players_by_account_id_histograms_by_field`
- Response codes: `200`
- Response schema: `200:array[object]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |
| `limit` | `query` | `no` | `integer` | Number of matches to limit to |
| `offset` | `query` | `no` | `integer` | Number of matches to offset start by |
| `win` | `query` | `no` | `integer` | Whether the player won |
| `patch` | `query` | `no` | `integer` | Patch ID, from dotaconstants |
| `game_mode` | `query` | `no` | `integer` | Game Mode ID |
| `lobby_type` | `query` | `no` | `integer` | Lobby type ID |
| `region` | `query` | `no` | `integer` | Region ID |
| `date` | `query` | `no` | `integer` | Days previous |
| `lane_role` | `query` | `no` | `integer` | Lane Role ID |
| `hero_id` | `query` | `no` | `integer` | Hero ID |
| `is_radiant` | `query` | `no` | `integer` | Whether the player was radiant |
| `included_account_id` | `query` | `no` | `integer` | Account IDs in the match (array) |
| `excluded_account_id` | `query` | `no` | `integer` | Account IDs not in the match (array) |
| `with_hero_id` | `query` | `no` | `integer` | Hero IDs on the player's team (array) |
| `against_hero_id` | `query` | `no` | `integer` | Hero IDs against the player's team (array) |
| `significant` | `query` | `no` | `integer` | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | `query` | `no` | `integer` | The minimum number of games played, for filtering hero stats |
| `sort` | `query` | `no` | `string` | The field to return matches sorted by in descending order |
| `field` | `path` | `yes` | `string` | Field to aggregate on |

### `GET /players/{account_id}/matches`

- Summary: GET /players/{account_id}/matches
- Description: Matches played (full history, and supports column selection)
- Operation ID: `get_players_by_account_id_select_matches`
- Response codes: `200`
- Response schema: `200:array[PlayerMatchesResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |
| `limit` | `query` | `no` | `integer` | Number of matches to limit to |
| `offset` | `query` | `no` | `integer` | Number of matches to offset start by |
| `win` | `query` | `no` | `integer` | Whether the player won |
| `patch` | `query` | `no` | `integer` | Patch ID, from dotaconstants |
| `game_mode` | `query` | `no` | `integer` | Game Mode ID |
| `lobby_type` | `query` | `no` | `integer` | Lobby type ID |
| `region` | `query` | `no` | `integer` | Region ID |
| `date` | `query` | `no` | `integer` | Days previous |
| `lane_role` | `query` | `no` | `integer` | Lane Role ID |
| `hero_id` | `query` | `no` | `integer` | Hero ID |
| `is_radiant` | `query` | `no` | `integer` | Whether the player was radiant |
| `included_account_id` | `query` | `no` | `integer` | Account IDs in the match (array) |
| `excluded_account_id` | `query` | `no` | `integer` | Account IDs not in the match (array) |
| `with_hero_id` | `query` | `no` | `integer` | Hero IDs on the player's team (array) |
| `against_hero_id` | `query` | `no` | `integer` | Hero IDs against the player's team (array) |
| `significant` | `query` | `no` | `integer` | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | `query` | `no` | `integer` | The minimum number of games played, for filtering hero stats |
| `sort` | `query` | `no` | `string` | The field to return matches sorted by in descending order |
| `project` | `query` | `no` | `string` | Fields to project (array) |

### `GET /players/{account_id}/peers`

- Summary: GET /players/{account_id}/peers
- Description: Players played with
- Operation ID: `get_players_by_account_id_select_peers`
- Response codes: `200`
- Response schema: `200:array[PlayerPeersResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |
| `limit` | `query` | `no` | `integer` | Number of matches to limit to |
| `offset` | `query` | `no` | `integer` | Number of matches to offset start by |
| `win` | `query` | `no` | `integer` | Whether the player won |
| `patch` | `query` | `no` | `integer` | Patch ID, from dotaconstants |
| `game_mode` | `query` | `no` | `integer` | Game Mode ID |
| `lobby_type` | `query` | `no` | `integer` | Lobby type ID |
| `region` | `query` | `no` | `integer` | Region ID |
| `date` | `query` | `no` | `integer` | Days previous |
| `lane_role` | `query` | `no` | `integer` | Lane Role ID |
| `hero_id` | `query` | `no` | `integer` | Hero ID |
| `is_radiant` | `query` | `no` | `integer` | Whether the player was radiant |
| `included_account_id` | `query` | `no` | `integer` | Account IDs in the match (array) |
| `excluded_account_id` | `query` | `no` | `integer` | Account IDs not in the match (array) |
| `with_hero_id` | `query` | `no` | `integer` | Hero IDs on the player's team (array) |
| `against_hero_id` | `query` | `no` | `integer` | Hero IDs against the player's team (array) |
| `significant` | `query` | `no` | `integer` | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | `query` | `no` | `integer` | The minimum number of games played, for filtering hero stats |
| `sort` | `query` | `no` | `string` | The field to return matches sorted by in descending order |

### `GET /players/{account_id}/pros`

- Summary: GET /players/{account_id}/pros
- Description: Pro players played with
- Operation ID: `get_players_by_account_id_select_pros`
- Response codes: `200`
- Response schema: `200:array[PlayerProsResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |
| `limit` | `query` | `no` | `integer` | Number of matches to limit to |
| `offset` | `query` | `no` | `integer` | Number of matches to offset start by |
| `win` | `query` | `no` | `integer` | Whether the player won |
| `patch` | `query` | `no` | `integer` | Patch ID, from dotaconstants |
| `game_mode` | `query` | `no` | `integer` | Game Mode ID |
| `lobby_type` | `query` | `no` | `integer` | Lobby type ID |
| `region` | `query` | `no` | `integer` | Region ID |
| `date` | `query` | `no` | `integer` | Days previous |
| `lane_role` | `query` | `no` | `integer` | Lane Role ID |
| `hero_id` | `query` | `no` | `integer` | Hero ID |
| `is_radiant` | `query` | `no` | `integer` | Whether the player was radiant |
| `included_account_id` | `query` | `no` | `integer` | Account IDs in the match (array) |
| `excluded_account_id` | `query` | `no` | `integer` | Account IDs not in the match (array) |
| `with_hero_id` | `query` | `no` | `integer` | Hero IDs on the player's team (array) |
| `against_hero_id` | `query` | `no` | `integer` | Hero IDs against the player's team (array) |
| `significant` | `query` | `no` | `integer` | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | `query` | `no` | `integer` | The minimum number of games played, for filtering hero stats |
| `sort` | `query` | `no` | `string` | The field to return matches sorted by in descending order |

### `GET /players/{account_id}/rankings`

- Summary: GET /players/{account_id}/rankings
- Description: Player hero rankings
- Operation ID: `get_players_by_account_id_select_rankings`
- Response codes: `200`
- Response schema: `200:array[PlayerRankingsResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |

### `GET /players/{account_id}/ratings`

- Summary: GET /players/{account_id}/ratings
- Description: Returns a history of the player rank tier/medal changes (replaces MMR)
- Operation ID: `get_players_by_account_id_select_ratings`
- Response codes: `200`
- Response schema: `200:array[PlayerRatingsResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |

### `GET /players/{account_id}/recentMatches`

- Summary: GET /players/{account_id}/recentMatches
- Description: Recent matches played (limited number of results)
- Operation ID: `get_players_by_account_id_select_recent_matches`
- Response codes: `200`
- Response schema: `200:array[object]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |

### `POST /players/{account_id}/refresh`

- Summary: POST /players/{account_id}/refresh
- Description: Refresh player match history (up to 500), medal (rank), and profile name
- Operation ID: `post_refresh`
- Response codes: `200`
- Response schema: `200:`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |

### `GET /players/{account_id}/totals`

- Summary: GET /players/{account_id}/totals
- Description: Totals in stats
- Operation ID: `get_players_by_account_id_select_totals`
- Response codes: `200`
- Response schema: `200:array[PlayerTotalsResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |
| `limit` | `query` | `no` | `integer` | Number of matches to limit to |
| `offset` | `query` | `no` | `integer` | Number of matches to offset start by |
| `win` | `query` | `no` | `integer` | Whether the player won |
| `patch` | `query` | `no` | `integer` | Patch ID, from dotaconstants |
| `game_mode` | `query` | `no` | `integer` | Game Mode ID |
| `lobby_type` | `query` | `no` | `integer` | Lobby type ID |
| `region` | `query` | `no` | `integer` | Region ID |
| `date` | `query` | `no` | `integer` | Days previous |
| `lane_role` | `query` | `no` | `integer` | Lane Role ID |
| `hero_id` | `query` | `no` | `integer` | Hero ID |
| `is_radiant` | `query` | `no` | `integer` | Whether the player was radiant |
| `included_account_id` | `query` | `no` | `integer` | Account IDs in the match (array) |
| `excluded_account_id` | `query` | `no` | `integer` | Account IDs not in the match (array) |
| `with_hero_id` | `query` | `no` | `integer` | Hero IDs on the player's team (array) |
| `against_hero_id` | `query` | `no` | `integer` | Hero IDs against the player's team (array) |
| `significant` | `query` | `no` | `integer` | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | `query` | `no` | `integer` | The minimum number of games played, for filtering hero stats |
| `sort` | `query` | `no` | `string` | The field to return matches sorted by in descending order |

### `GET /players/{account_id}/wardmap`

- Summary: GET /players/{account_id}/wardmap
- Description: Wards placed in matches played
- Operation ID: `get_players_by_account_id_select_wardmap`
- Response codes: `200`
- Response schema: `200:PlayerWardMapResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |
| `limit` | `query` | `no` | `integer` | Number of matches to limit to |
| `offset` | `query` | `no` | `integer` | Number of matches to offset start by |
| `win` | `query` | `no` | `integer` | Whether the player won |
| `patch` | `query` | `no` | `integer` | Patch ID, from dotaconstants |
| `game_mode` | `query` | `no` | `integer` | Game Mode ID |
| `lobby_type` | `query` | `no` | `integer` | Lobby type ID |
| `region` | `query` | `no` | `integer` | Region ID |
| `date` | `query` | `no` | `integer` | Days previous |
| `lane_role` | `query` | `no` | `integer` | Lane Role ID |
| `hero_id` | `query` | `no` | `integer` | Hero ID |
| `is_radiant` | `query` | `no` | `integer` | Whether the player was radiant |
| `included_account_id` | `query` | `no` | `integer` | Account IDs in the match (array) |
| `excluded_account_id` | `query` | `no` | `integer` | Account IDs not in the match (array) |
| `with_hero_id` | `query` | `no` | `integer` | Hero IDs on the player's team (array) |
| `against_hero_id` | `query` | `no` | `integer` | Hero IDs against the player's team (array) |
| `significant` | `query` | `no` | `integer` | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | `query` | `no` | `integer` | The minimum number of games played, for filtering hero stats |
| `sort` | `query` | `no` | `string` | The field to return matches sorted by in descending order |

### `GET /players/{account_id}/wl`

- Summary: GET /players/{account_id}/wl
- Description: Win/Loss count
- Operation ID: `get_players_by_account_id_select_wl`
- Response codes: `200`
- Response schema: `200:PlayerWinLossResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |
| `limit` | `query` | `no` | `integer` | Number of matches to limit to |
| `offset` | `query` | `no` | `integer` | Number of matches to offset start by |
| `win` | `query` | `no` | `integer` | Whether the player won |
| `patch` | `query` | `no` | `integer` | Patch ID, from dotaconstants |
| `game_mode` | `query` | `no` | `integer` | Game Mode ID |
| `lobby_type` | `query` | `no` | `integer` | Lobby type ID |
| `region` | `query` | `no` | `integer` | Region ID |
| `date` | `query` | `no` | `integer` | Days previous |
| `lane_role` | `query` | `no` | `integer` | Lane Role ID |
| `hero_id` | `query` | `no` | `integer` | Hero ID |
| `is_radiant` | `query` | `no` | `integer` | Whether the player was radiant |
| `included_account_id` | `query` | `no` | `integer` | Account IDs in the match (array) |
| `excluded_account_id` | `query` | `no` | `integer` | Account IDs not in the match (array) |
| `with_hero_id` | `query` | `no` | `integer` | Hero IDs on the player's team (array) |
| `against_hero_id` | `query` | `no` | `integer` | Hero IDs against the player's team (array) |
| `significant` | `query` | `no` | `integer` | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | `query` | `no` | `integer` | The minimum number of games played, for filtering hero stats |
| `sort` | `query` | `no` | `string` | The field to return matches sorted by in descending order |

### `GET /players/{account_id}/wordcloud`

- Summary: GET /players/{account_id}/wordcloud
- Description: Words said/read in matches played
- Operation ID: `get_players_by_account_id_select_wordcloud`
- Response codes: `200`
- Response schema: `200:PlayerWordCloudResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `path` | `yes` | `integer` | Steam32 account ID |
| `limit` | `query` | `no` | `integer` | Number of matches to limit to |
| `offset` | `query` | `no` | `integer` | Number of matches to offset start by |
| `win` | `query` | `no` | `integer` | Whether the player won |
| `patch` | `query` | `no` | `integer` | Patch ID, from dotaconstants |
| `game_mode` | `query` | `no` | `integer` | Game Mode ID |
| `lobby_type` | `query` | `no` | `integer` | Lobby type ID |
| `region` | `query` | `no` | `integer` | Region ID |
| `date` | `query` | `no` | `integer` | Days previous |
| `lane_role` | `query` | `no` | `integer` | Lane Role ID |
| `hero_id` | `query` | `no` | `integer` | Hero ID |
| `is_radiant` | `query` | `no` | `integer` | Whether the player was radiant |
| `included_account_id` | `query` | `no` | `integer` | Account IDs in the match (array) |
| `excluded_account_id` | `query` | `no` | `integer` | Account IDs not in the match (array) |
| `with_hero_id` | `query` | `no` | `integer` | Hero IDs on the player's team (array) |
| `against_hero_id` | `query` | `no` | `integer` | Hero IDs against the player's team (array) |
| `significant` | `query` | `no` | `integer` | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. |
| `having` | `query` | `no` | `integer` | The minimum number of games played, for filtering hero stats |
| `sort` | `query` | `no` | `string` | The field to return matches sorted by in descending order |

## pro matches
<a id="pro-matches"></a>

### `GET /proMatches`

- Summary: GET /proMatches
- Description: Get list of pro matches
- Operation ID: `get_pro_matches`
- Response codes: `200`
- Response schema: `200:array[MatchObjectResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `less_than_match_id` | `query` | `no` | `integer` | Get matches with a match ID lower than this value |

## pro players
<a id="pro-players"></a>

### `GET /proPlayers`

- Summary: GET /proPlayers
- Description: Get list of pro players
- Operation ID: `get_pro_players`
- Response codes: `200`
- Response schema: `200:array[PlayerObjectResponse]`

No documented parameters.

## public matches
<a id="public-matches"></a>

### `GET /publicMatches`

- Summary: GET /publicMatches
- Description: Get list of randomly sampled public matches
- Operation ID: `get_public_matches`
- Response codes: `200`
- Response schema: `200:array[PublicMatchesResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `less_than_match_id` | `query` | `no` | `integer` | Get matches with a match ID lower than this value |
| `min_rank` | `query` | `no` | `integer` | Minimum rank for the matches. Ranks are represented by integers (10-15: Herald, 20-25: Guardian, 30-35: Crusader, 40-45: Archon, 50-55: Legend, 60-65: Ancient, 70-75: Divine, 80: Immortal). Each increment represents an additional star. |
| `max_rank` | `query` | `no` | `integer` | Maximum rank for the matches. Ranks are represented by integers (10-15: Herald, 20-25: Guardian, 30-35: Crusader, 40-45: Archon, 50-55: Legend, 60-65: Ancient, 70-75: Divine, 80: Immortal). Each increment represents an additional star. |

## rankings
<a id="rankings"></a>

### `GET /rankings`

- Summary: GET /rankings
- Description: Top players by hero
- Operation ID: `get_rankings`
- Response codes: `200`
- Response schema: `200:RankingsResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `hero_id` | `query` | `yes` | `string` | Hero ID |

## records
<a id="records"></a>

### `GET /records/{field}`

- Summary: GET /records/{field}
- Description: Get top performances in a stat
- Operation ID: `get_records_by_field`
- Response codes: `200`
- Response schema: `200:array[RecordsResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `field` | `path` | `yes` | `string` | Field name to query |

## request
<a id="request"></a>

### `GET /request/{jobId}`

- Summary: GET /request/{jobId}
- Description: Get parse request state
- Operation ID: `get_request_by_job_id`
- Response codes: `200`
- Response schema: `200:object`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `jobId` | `path` | `yes` | `string` | The job ID to query. |

### `POST /request/{match_id}`

- Summary: POST /request/{match_id}
- Description: Submit a new parse request. This call counts as 10 calls for rate limit (but not billing) purposes.
- Operation ID: `post_request_by_job_id`
- Response codes: `200`
- Response schema: `200:object`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `match_id` | `path` | `yes` | `integer` | - |

## scenarios
<a id="scenarios"></a>

### `GET /scenarios/itemTimings`

- Summary: GET /scenarios/itemTimings
- Description: Win rates for certain item timings on a hero for items that cost at least 1400 gold
- Operation ID: `get_scenarios_item_timings`
- Response codes: `200`
- Response schema: `200:array[ScenarioItemTimingsResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `item` | `query` | `no` | `string` | Filter by item name e.g. "spirit_vessel" |
| `hero_id` | `query` | `no` | `integer` | Hero ID |

### `GET /scenarios/laneRoles`

- Summary: GET /scenarios/laneRoles
- Description: Win rates for heroes in certain lane roles
- Operation ID: `get_scenarios_lane_roles`
- Response codes: `200`
- Response schema: `200:array[ScenarioLaneRolesResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `lane_role` | `query` | `no` | `string` | Filter by lane role 1-4 (Safe, Mid, Off, Jungle) |
| `hero_id` | `query` | `no` | `integer` | Hero ID |

### `GET /scenarios/misc`

- Summary: GET /scenarios/misc
- Description: Miscellaneous team scenarios
- Operation ID: `get_scenarios_misc`
- Response codes: `200`
- Response schema: `200:array[ScenarioMiscResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `scenario` | `query` | `no` | `string` | Name of the scenario (see teamScenariosQueryParams) |

## schema
<a id="schema"></a>

### `GET /schema`

- Summary: GET /schema
- Description: Get database schema
- Operation ID: `get_schema`
- Response codes: `200`
- Response schema: `200:array[SchemaResponse]`

No documented parameters.

## search
<a id="search"></a>

### `GET /search`

- Summary: GET /search
- Description: Search players by personaname.
- Operation ID: `get_search`
- Response codes: `200`
- Response schema: `200:array[SearchResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `q` | `query` | `yes` | `string` | Search string |

## teams
<a id="teams"></a>

### `GET /teams`

- Summary: GET /teams
- Description: Get team data
- Operation ID: `get_teams`
- Response codes: `200`
- Response schema: `200:array[TeamObjectResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `page` | `query` | `no` | `integer` | Page number, zero indexed. Each page returns up to 1000 entries. |

### `GET /teams/{team_id}`

- Summary: GET /teams/{team_id}
- Description: Get data for a team
- Operation ID: `get_teams_by_team_id`
- Response codes: `200`
- Response schema: `200:TeamObjectResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `path` | `yes` | `integer` | Team ID |

### `GET /teams/{team_id}/heroes`

- Summary: GET /teams/{team_id}/heroes
- Description: Get heroes for a team
- Operation ID: `get_teams_by_team_id_select_heroes`
- Response codes: `200`
- Response schema: `200:TeamHeroesResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `path` | `yes` | `integer` | Team ID |

### `GET /teams/{team_id}/matches`

- Summary: GET /teams/{team_id}/matches
- Description: Get matches for a team
- Operation ID: `get_teams_by_team_id_select_matches`
- Response codes: `200`
- Response schema: `200:TeamMatchObjectResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `path` | `yes` | `integer` | Team ID |

### `GET /teams/{team_id}/players`

- Summary: GET /teams/{team_id}/players
- Description: Get players who have played for a team
- Operation ID: `get_teams_by_team_id_select_players`
- Response codes: `200`
- Response schema: `200:TeamPlayersResponse`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `path` | `yes` | `integer` | Team ID |

## top players
<a id="top-players"></a>

### `GET /topPlayers`

- Summary: GET /topPlayers
- Description: Get list of highly ranked players
- Operation ID: `get_top_players`
- Response codes: `200`
- Response schema: `200:array[PlayerObjectResponse]`

| Parameter | In | Required | Schema | Description |
| --- | --- | --- | --- | --- |
| `turbo` | `query` | `no` | `integer` | Get ratings based on turbo matches |
