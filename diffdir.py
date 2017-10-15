#!/usr/bin/env python
"""
Pure Python stdlib directory comparison by filename
"""
from pathlib import Path
import filecmp

def diffdir(path1:Path, path2:Path):
    path1 = Path(path1).expanduser()
    path2 = Path(path2).expanduser()
    
    diff = filecmp.dircmp(path1, path2)
    print('\n'.join(diff.diff_files),end="")
    print('\n'.join(diff.left_only),end="")
    print('\n'.join(diff.right_only),end="")
# %% fix exit prompt position
    if any([diff.diff_files,diff.left_only,diff.right_only]):
        print()

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('path1', help='first path to compare')
    p.add_argument('path2', help='second path to compare')
    p = p.parse_args()
    
    diffdir(p.path1, p.path2)