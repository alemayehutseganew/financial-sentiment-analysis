"""Run basic EDA from command line.
Usage: python scripts/run_eda.py path/to/news.csv
"""
import sys
from src.data_loader import load_news_csv
from src.eda import headline_length_stats, publisher_counts

def main(path):
    df = load_news_csv(path)
    print('Headline length stats:', headline_length_stats(df))
    print('\nTop publishers:\n', publisher_counts(df))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python scripts/run_eda.py path/to/news.csv')
    else:
        main(sys.argv[1])
