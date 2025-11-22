from src.sentiment import score_headlines_df
import pandas as pd

def test_text_scoring_default():
    df = pd.DataFrame({'headline': ['Company beats estimates', 'Company misses target', 'Neutral statement']})
    scored = score_headlines_df(df)
    assert 'sentiment_score' in scored.columns
