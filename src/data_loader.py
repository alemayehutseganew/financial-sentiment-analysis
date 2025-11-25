"""Utility helpers for loading the news and OHLCV CSV assets.

Each loader guards against missing files, coerces the timestamp column
into ``datetime64[ns]`` for downstream joins, and returns a clean
``pandas.DataFrame`` ready for sentiment scoring or indicator math.
"""
from pathlib import Path

import pandas as pd


def load_news_csv(path: str, date_col: str = 'date') -> pd.DataFrame:
    """Load and timestamp-normalize a news CSV.

    Args:
        path: Absolute/relative path to ``raw_analyst_ratings`` style CSV.
        date_col: Name of the column containing publication timestamps.

    Returns:
        DataFrame with ``date_col`` parsed via ``pd.to_datetime`` so the
        calling code can safely drop timezone info or align by trading day.
    """

    resolved_path = Path(path)
    if not resolved_path.exists():
        raise FileNotFoundError(f'News CSV not found at: {resolved_path}')
    df = pd.read_csv(resolved_path)
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    return df


def load_price_csv(path: str, date_col: str = 'Date') -> pd.DataFrame:
    """Load OHLCV data from disk, sorted by session date.

    Args:
        path: Absolute/relative path to a ticker CSV (e.g., ``data/AAPL.csv``).
        date_col: Name of the column storing trade dates (defaults to ``Date``).

    Returns:
        DataFrame with chronological ordering and a parsed ``date_col`` so
        percentage-change or indicator helpers can rely on monotonic dates.
    """

    resolved_path = Path(path)
    if not resolved_path.exists():
        raise FileNotFoundError(f'Price CSV not found at: {resolved_path}')
    df = pd.read_csv(resolved_path)
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.sort_values(date_col).reset_index(drop=True)
    return df
