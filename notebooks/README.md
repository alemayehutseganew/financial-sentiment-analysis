# Notebooks Overview

This folder hosts the Task 1 exploratory notebooks plus the Task 2 quantitative analysis workbook. Each notebook is self-contained (no dependency on missing `src` helpers) so you can run them directly after installing the requirements.

| Notebook | Purpose | Inputs |
| --- | --- | --- |
| `01_eda.ipynb` | Descriptive statistics, publisher profiling, temporal trends, topic modeling | `data/raw_analyst_ratings.csv` |
| `02_sentiment_analysis.ipynb` | TextBlob/VADER scoring + aggregated sentiment tables (daily + publisher) | `data/raw_analyst_ratings.csv` |
| `03_technical_indicators.ipynb` | Rolling SMA/RSI/MACD indicator calculations with pandas | `data/AAPL.csv` (swap for `AMZN`, `GOOG`, `NVDA`, etc.) |
| `04_correlation_analysis.ipynb` | Joins aggregated sentiment with price returns and reports Pearson correlation | `data/raw_analyst_ratings.csv`, `data/AAPL.csv` |
| `05_quant_analysis.ipynb` | TA-Lib indicators + PyNance risk/return metrics with multi-panel plots | `data/AAPL.csv` (swap for other tickers) |

## Usage

1. Activate the virtual environment and run `pip install -r ../requirements.txt` from the repo root.
2. Launch Jupyter Lab/VS Code notebooks.
3. Run each notebook top-to-bottom; every file prints intermediate tables so you can export them if needed.
4. To target another ticker, change the `price_path` (and optionally `news` path) near the top of the relevant notebook.

> Keep the executed notebooks committed on the `task-1` branch with informative commit messages—a Task 1 KPI is evidence of relevant skills and experiment tracking.
