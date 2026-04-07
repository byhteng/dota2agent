# AGENTS.md

## Project goal
- This project is for Dota 2 public data collection and analysis.
- Prefer reproducible scripts over one-off manual steps.

## Working rules
- Before writing code, first inspect the target API or documentation.
- Save all raw API responses to `data/raw/`.
- Save cleaned tables to `data/processed/`.
- Put analysis scripts in `scripts/`.
- Do not overwrite existing raw data unless explicitly requested.

## Execution rules
- When downloading data, use small test samples first.
- If a command may fail because of missing dependencies, explain the dependency and propose the install command.
- After writing a script, show how to run it with one concrete example.

## Output expectations
- Summaries should include:
  - data source
  - sample size
  - assumptions
  - limitations
- For BP analysis, separate raw observations from interpretation.