import pandas as pd
from pathlib import Path


def parse_tsv(filename):
    """"
    A parser for tsv files

    :param filename: String, name of the file
    :return: dataframe object
    """


    file = Path(__file__, f'../data/{filename}').resolve()
    df = pd.read_csv(file, sep='\t')
    return df
