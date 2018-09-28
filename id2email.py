#!/usr/bin/env python
"""
convert spreadsheet email ID list to email addresses
"""
import pandas
from argparse import ArgumentParser
from pathlib import Path
import numpy as np


def main():
    p = ArgumentParser()
    p.add_argument('fn', help='.xlsx filename')
    p.add_argument('domain', help='@domain.com')
    p = p.parse_args()

    ids = pandas.read_excel(Path(p.fn).expanduser(), usecols="A,B").dropna()
    ids = np.append(ids.iloc[:, 0].values, ids.iloc[:, 1].values)

    emails = (ids + f'@{p.domain}').tolist()

    print('; '.join(emails))


if __name__ == '__main__':
    main()
