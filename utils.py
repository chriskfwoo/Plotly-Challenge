import pandas as pd
from pathlib import Path


def parse_tsv():
    file = Path(__file__, "../data/mtcars.tsv").resolve()
    df = pd.read_table(file)

    return df
