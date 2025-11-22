import pytest
from src.data_loader import load_news_csv

def test_loader_file_not_found():
    import os
    with pytest.raises(FileNotFoundError):
        load_news_csv('nonexistent_news.csv')
