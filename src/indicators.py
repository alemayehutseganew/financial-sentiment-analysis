"""indicators.py
Compute simple technical indicators using pandas (pure Python fallback implementations).
"""
import pandas as pd
import numpy as np
from typing import Optional

def add_moving_average(df: pd.DataFrame, price_col: str = 'Close', window: int = 20, col_name: Optional[str] = None):
    col_name = col_name or f'MA_{window}'
    df[col_name] = df[price_col].rolling(window=window, min_periods=1).mean()
    return df

def add_rsi(df: pd.DataFrame, price_col: str = 'Close', window: int = 14, col_name: Optional[str] = None):
    col_name = col_name or f'RSI_{window}'
    delta = df[price_col].diff()
    gain = delta.clip(lower=0).fillna(0)
    loss = -delta.clip(upper=0).fillna(0)
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    rs = avg_gain / (avg_loss.replace(0, np.nan))
    rsi = 100 - (100 / (1 + rs))
    df[col_name] = rsi.fillna(50)
    return df

def add_macd(df: pd.DataFrame, price_col: str = 'Close', fast: int = 12, slow: int = 26, signal: int = 9):
    ema_fast = df[price_col].ewm(span=fast, adjust=False).mean()
    ema_slow = df[price_col].ewm(span=slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    macd_signal = macd.ewm(span=signal, adjust=False).mean()
    df['MACD'] = macd
    df['MACD_signal'] = macd_signal
    df['MACD_hist'] = df['MACD'] - df['MACD_signal']
    return df
