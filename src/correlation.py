"""correlation.py
Utilities to align sentiment and price data and compute correlations.
"""
import pandas as pd

def compute_daily_returns(price_df: pd.DataFrame, date_col: str = 'Date', close_col: str = 'Close'):
    df = price_df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col).reset_index(drop=True)
    df['daily_return'] = df[close_col].pct_change()
    return df

def aggregate_daily_sentiment(news_df: pd.DataFrame, date_col: str = 'date', score_col: str = 'sentiment_score'):
    df = news_df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    agg = df.groupby(df[date_col].dt.date)[score_col].mean().reset_index()
    agg.rename(columns={date_col: 'date', score_col: 'avg_sentiment'}, inplace=True)
    agg['date'] = pd.to_datetime(agg['date'])
    return agg

def merge_sentiment_returns(sent_agg_df: pd.DataFrame, returns_df: pd.DataFrame, left_on: str = 'date', right_on: str = 'Date'):
    merged = pd.merge(sent_agg_df, returns_df, left_on=left_on, right_on=right_on, how='inner')
    return merged

def pearson_correlation(merged_df: pd.DataFrame, sentiment_col: str = 'avg_sentiment', return_col: str = 'daily_return'):
    return merged_df[[sentiment_col, return_col]].corr().iloc[0,1]
