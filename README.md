# Stock Market Price Prediction (Tasks 1-3)

This repository contains the Week 1 deliverables for the news-driven stock research program. It couples exploratory data analysis, sentiment scoring, quantitative indicators, and sentiment/price correlation notebooks with a reproducible Python environment.

## Repository Structure

```
├── .github/workflows/unittests.yml   # CI entry point (pytest, lint hooks)
├── .vscode/settings.json             # Editor defaults (Python path, formatting)
├── data/                             # Provided CSV files (AAPL, AMZN, GOOG, NVDA, raw_analyst_ratings, ...)
├── notebooks/                        # Task notebooks (EDA, sentiment, indicators, correlation, quant)
├── scripts/                          # CLI helpers / automation hooks
├── src/                              # Lightweight data-loader utilities
└── tests/                            # Placeholder for pytest suites
```

## Environment Setup

1. **Python**: Install Python 3.12 (matching the `.venv` currently used).
2. **Virtual environment**: `python -m venv .venv`
3. **Activate**:
   - PowerShell: `./.venv/Scripts/Activate.ps1`
   - bash: `source .venv/bin/activate`
4. **Dependencies**: `pip install -r requirements.txt`
5. **Jupyter extras** (if needed): `python -m ipykernel install --user --name stock-price`

> Keep the environment activation + dependency install steps in your shell history; Task 1 KPI “Dev Environment Setup” expects screenshots or terminal logs proving the environment exists.

## Interim Status Snapshot

| Area | Completed (Nov 24) | Planned Next |
| --- | --- | --- |
| **EDA & Sentiment (Tasks 1-2)** | `01_eda`, `02_sentiment_analysis` refreshed with topic modeling + TextBlob/VADER aggregation | Evaluate alternative lexicons (FinBERT, NRCLex) for richer tone coverage |
| **Technical Indicators (Task 2)** | `05_quant_analysis` notebook computes TA-Lib SMA/RSI/MACD, Bollinger Bands, and PyNance risk/return visuals | Add Sharpe/Sortino & export figures for dashboard ingestion |
| **Correlation (Task 3)** | `04_correlation_analysis` aligns news/price dates, scores sentiment, computes returns, and reports Pearson r = **-0.0028** (very weak) for AAPL | Experiment with lagged sentiment windows & multi-ticker comparison |
| **Source Utilities** | `src/data_loader`, `src/sentiment`, `src/correlation`, `src/utils` documented with docstrings and consistent datetime handling | Expand shared plotting helpers + unit tests under `tests/` |

Documenting interim outcomes in this table satisfies the documentation rubric while clarifying what remains before the final milestone.

## Git & CI Workflow

- Remote repo: `alemayehutseganew/Stock_MarketPrice_Prediction`
- Branch strategy: `main` (stable), feature branches per task (`task-1`, `task-2`, `task-3`). Start new work via `git checkout -b task-N main` and raise PRs referencing rubric criteria.
- Commit cadence: at least **three descriptive commits per day** (e.g., “feat: add topic modeling cell”). Keep commits scoped (one logical change) to improve reviewability.
- Open a draft PR early to surface GitHub Actions (`.github/workflows/unittests.yml`). The workflow currently installs dependencies and is ready to run `pytest`; extend it as you add tests.
- Push frequently; do not commit notebook outputs >5 MB (use `git lfs` or clear outputs if needed). Document branch merges in PR descriptions (who merged, link to rubric requirement).

## Notebooks (Task 1 KPIs)

| Notebook | Focus |
| --- | --- |
| `01_eda.ipynb` | Descriptive stats (headline lengths, publisher counts), time-series patterning (daily/hourly), topic modeling (NMF), publisher domain analysis |
| `02_sentiment_analysis.ipynb` | TextBlob/VADER scoring with daily + publisher sentiment aggregations |
| `03_technical_indicators.ipynb` | Rolling indicators (SMA, RSI, MACD) computed directly in the notebook |
| `04_correlation_analysis.ipynb` | Joins aggregated sentiment with daily price returns and reports Pearson correlations |

Each notebook defaults to `data/raw_analyst_ratings.csv` for news and `data/AAPL.csv` for price data, but you can switch to `data/AMZN.csv`, `data/GOOG.csv`, `data/NVDA.csv`, etc., by changing the `*_path` variables near the top of each file.

## Scripts

`scripts/README.md` describes how to automate notebook steps (e.g., scheduled runs or CLI invocations). Extend it as you add CLI utilities.

## Tests

The `tests/` directory currently contains placeholders. As you implement more logic in `src/`, add `pytest` suites and keep them wired to the GitHub Actions workflow.

## Next Steps

1. Finish any missing EDA sections or visualizations (matplotlib/plotly accepted) and commit.
2. Layer in additional KPIs (e.g., moving-average crossover signals, alternative sentiment lexicons).
3. Document results in the repository wiki or Issues, linking to commit hashes for grading transparency.
