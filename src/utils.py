"""utils.py
Small utility helpers used across modules.
"""
from datetime import datetime

def ensure_utc(dt):
    if dt.tzinfo is None:
        return dt
    return dt.astimezone(tz=None)
