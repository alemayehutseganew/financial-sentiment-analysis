"""data_loader.py
Simple utilities to load news CSV and price CSV datasets.
"""
from typing import Optional
import pandas as pd
import os

def load_news_csv(path: str, date_col: str = 'date') -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f'News CSV not found at: {path}')
    df = pd.read_csv('C:/Users/alexo/Desktop/File/10Academy/week1/Data/newsData/raw_analyst_ratings.csv')
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    return df

def load_price_csv(path: str, date_col: str = 'Date') -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f'Price CSV not found at: {path}')
    df = pd.read_csv(path)
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.sort_values(date_col).reset_index(drop=True)
    return df
