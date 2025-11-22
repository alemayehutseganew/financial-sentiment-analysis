"""Compute indicators on price CSV and save result"""
import sys
from src.data_loader import load_price_csv
from src.indicators import add_moving_average, add_rsi, add_macd

def main(inpath, outpath):
    df = load_price_csv(inpath)
    df = add_moving_average(df, window=20)
    df = add_rsi(df, window=14)
    df = add_macd(df)
    df.to_csv(outpath, index=False)
    print('Saved indicators to', outpath)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python scripts/run_indicators.py price.csv out.csv')
    else:
        main(sys.argv[1], sys.argv[2])
