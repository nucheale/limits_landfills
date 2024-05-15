import pandas as pd


def is_date(string):
    try:
        pd.to_datetime(string)
        return True
    except (TypeError, ValueError):
        return False
