from src.indicators import add_moving_average, add_rsi, add_macd
import pandas as pd

def test_indicators_basic():
    df = pd.DataFrame({'Close': [1,2,3,2,3,4,5]})
    df = add_moving_average(df, window=3)
    df = add_rsi(df, window=3)
    df = add_macd(df)
    assert 'MA_3' in df.columns
    assert 'RSI_3' in df.columns
    assert 'MACD' in df.columns
