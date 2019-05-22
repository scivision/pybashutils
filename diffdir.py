#!/usr/bin/env python
"""
Pure Python stdlib directory comparison by filename
"""
from pathlib import Path
import filecmp
from argparse import ArgumentParser


def diff_dir(path1: Path, path2: Path):
    path1 = Path(path1).expanduser()
    path2 = Path(path2).expanduser()

    if path1.samefile(path2):
        raise OSError(f'you are comparing {path1} with itself!')

    diff = filecmp.dircmp(path1, path2)  # type: ignore
    print('\n'.join(diff.diff_files), end="")  # type: ignore
    print('\n'.join(diff.left_only), end="")  # type: ignore
    print('\n'.join(diff.right_only), end="")  # type: ignore
# %% fix exit prompt position
    if any([diff.diff_files, diff.left_only, diff.right_only]):
        print()


def main():
    p = ArgumentParser()
    p.add_argument('path1', help='first path to compare')
    p.add_argument('path2', help='second path to compare')
    P = p.parse_args()

    diff_dir(P.path1, P.path2)


if __name__ == '__main__':
    main()
