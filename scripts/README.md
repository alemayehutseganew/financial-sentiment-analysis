# Scripts

The `scripts/` folder is reserved for lightweight automation helpers that mirror what the notebooks do, making it easier to schedule runs or wire them into CI.

## Current Files

- `full_correlation_run.log` – sample log output from a previous batch run (kept for reference).
- `__init__.py` – allows importing `scripts` as a package when needed.

## How to Add a Script

1. Create a new Python file (for example `run_eda.py`).
2. Inside the script, reuse the logic from the notebooks (import from `src.data_loader`, compute indicators, etc.).
3. Accept CLI arguments via `argparse` so you can point at different CSVs: `python scripts/run_eda.py --news data/raw_analyst_ratings.csv`.
4. Log progress to stdout and optionally to a timestamped file inside `scripts/logs/` (add this folder if you need it).

## Suggested Automation Ideas

- **Scheduled Data Refresh**: pull the latest CSVs, append to `data/`, then rerun notebooks.
- **Sentiment Batch Job**: nightly job that scores the latest headlines and dumps them to `outputs/sentiment_<date>.csv`.
- **Correlation Monitor**: script that recomputes the sentiment/price correlation for every ticker in `data/` and posts the results (JSON/CSV) for dashboards.

Whenever you add a new script, mention it in the root `README.md` and consider referencing it from the GitHub Actions workflow if it should run on every push.
