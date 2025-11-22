"""Run sentiment scorer from command line."""
import sys
from src.data_loader import load_news_csv
from src.sentiment import score_headlines_df

def main(inpath, outpath):
    df = load_news_csv(inpath)
    df = score_headlines_df(df, method='textblob')
    df.to_csv(outpath, index=False)
    print('Saved scored headlines to', outpath)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python scripts/run_sentiment.py path/to/news.csv output.csv')
    else:
        main(sys.argv[1], sys.argv[2])
