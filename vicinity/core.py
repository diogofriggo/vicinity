import os
import csv
from functools import lru_cache
from pathlib import Path

import pandas as pd

@lru_cache(maxsize=None)
def cached_read_csv(file_path):
    with open(file_path) as file:
        sep = csv.Sniffer().sniff(file.readline()).delimiter

    return pd.read_csv(file_path, sep=sep)