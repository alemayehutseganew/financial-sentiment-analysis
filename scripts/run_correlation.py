"""Aggregate sentiment and compute correlation with returns."""
import sys
from src.data_loader import load_news_csv, load_price_csv
from src.sentiment import score_headlines_df
from src.correlation import compute_daily_returns, aggregate_daily_sentiment, merge_sentiment_returns, pearson_correlation

def main(news_csv, price_csv):
    news = load_news_csv(news_csv)
    news = score_headlines_df(news)
    price = load_price_csv(price_csv)
    returns = compute_daily_returns(price)
    sent_agg = aggregate_daily_sentiment(news)
    merged = merge_sentiment_returns(sent_agg, returns, left_on='date', right_on='Date')
    corr = pearson_correlation(merged)
    print('Pearson correlation (avg_sentiment, daily_return):', corr)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python scripts/run_correlation.py news.csv price.csv')
    else:
        main(sys.argv[1], sys.argv[2])
