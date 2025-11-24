"""data_loader.py
Simple utilities to load news CSV and price CSV datasets.
"""
from typing import Optional
import os
from pathlib import Path
import pandas as pd

def load_news_csv(path: str, date_col: str = 'date') -> pd.DataFrame:
    resolved_path = Path(path)
    if not resolved_path.exists():
        raise FileNotFoundError(f'News CSV not found at: {resolved_path}')
    df = pd.read_csv(resolved_path)
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    return df

def load_price_csv(path: str, date_col: str = 'Date') -> pd.DataFrame:
    resolved_path = Path(path)
    if not resolved_path.exists():
        raise FileNotFoundError(f'Price CSV not found at: {resolved_path}')
    df = pd.read_csv(resolved_path)
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.sort_values(date_col).reset_index(drop=True)
    return df
