#!/usr/bin/env python
"""
compare binary output files
"""
import filecmp
from pathlib import Path


def compbin(dir1: Path, dir2: Path, pat: str):
    dir1 = Path(dir1).expanduser()
    dir2 = Path(dir2).expanduser()

    fl1 = dir1.glob(pat)
    fl2 = dir2.glob(pat)

    for f, g in zip(fl1, fl2):
        if not filecmp.cmp(f, g, False):
            print('difference:', f.name)


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument(
        'dirs', help='dir1 dir2 to compare files matching pat', nargs=2)
    p.add_argument('pat', help='filename pattern')
    P = p.parse_args()

    compbin(P.dirs[0], P.dirs[1], P.pat)
