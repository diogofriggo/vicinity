from functools import lru_cache

import pandas as pd


@lru_cache(maxsize=None)
def read_cached_csv(file_path):
    return pd.read_csv(file_path, sep=';', encoding='utf_16_le')