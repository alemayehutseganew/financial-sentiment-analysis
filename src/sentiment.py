"""sentiment.py
Small wrapper to compute sentiment scores using TextBlob and optional VADER.
"""
from typing import Optional
import pandas as pd

def score_headlines_df(df: pd.DataFrame, text_col: str = 'headline', method: str = 'textblob') -> pd.DataFrame:
    """Annotate a DataFrame with sentiment scores using TextBlob or VADER."""

    df = df.copy()
    if method == 'vader':
        try:
            from nltk.sentiment import SentimentIntensityAnalyzer
        except Exception:
            raise RuntimeError('VADER not available; please install nltk and download vader_lexicon')
        sia = SentimentIntensityAnalyzer()
        df['sentiment_score'] = df[text_col].fillna('').astype(str).map(lambda t: sia.polarity_scores(t)['compound'])
    else:
        try:
            from textblob import TextBlob
        except Exception:
            # fallback simple rule-based polarity
            df['sentiment_score'] = df[text_col].fillna('').astype(str).map(
                lambda s: 1.0 if 'up' in s.lower() or 'beat' in s.lower()
                else (-1.0 if 'drop' in s.lower() or 'miss' in s.lower() else 0.0)
            )
            return df
        df['sentiment_score'] = df[text_col].fillna('').astype(str).map(lambda t: TextBlob(t).sentiment.polarity)
    return df
