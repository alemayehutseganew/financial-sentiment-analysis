"""eda.py
Exploratory data analysis helper functions.
"""
import pandas as pd

def headline_length_stats(news_df: pd.DataFrame, col: str = 'headline'):
    s = news_df[col].dropna().astype(str).str.split().str.len()
    return {
        'count': int(s.count()),
        'min_words': int(s.min()),
        'max_words': int(s.max()),
        'mean_words': float(s.mean()),
        'median_words': float(s.median())
    }

def publisher_counts(news_df: pd.DataFrame, publisher_col: str = 'publisher', top_n: int = 10):
    return news_df[publisher_col].value_counts().head(top_n)

