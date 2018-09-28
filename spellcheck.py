#!/usr/bin/env python
"""
Ctrl \  to abort
"""
from subprocess import check_call
from pathlib import Path
from typing import List, Union
from argparse import ArgumentParser

MAXSIZE = 20e6  # [bytes]


def findtext(root: Union[Path, str], globext: List[str], exclude: List[str],
             verbose: bool = False):
    """finds file to spell check"""
    if isinstance(globext, (Path, str)):
        globext = [globext]

    for e in globext:
        # in case "ext" is actually a specific filename
        ext = Path(e).expanduser()
        if ext.is_file():
            spellchk(ext)
        else:  # usual case
            spellchklist(list(Path(root).expanduser().rglob(str(ext))), exclude, verbose)


def spellchklist(flist: List[Path], exclude: List[str], verbose: bool = False):
    """Spell check each file"""
    if verbose:
        print(f'spell checking {flist}')

    for f in flist:
        spellchk(f, exclude)


def spellchk(f: Path, exclude: List[str] = None):

    if exclude is not None:
        for ex in exclude:
            if f.parent.name.endswith(ex):
                return

    try:
        check_call(['aspell', 'check', str(f)])
    except Exception as e:  # catch-all for unexpected error
        print(f, e)


def main():
    p = ArgumentParser(description='searches for TEXT under DIR and echos back filenames')
    p.add_argument('rdir', help='root dir to search', nargs='?', default='.')
    p.add_argument('-g', '--glob', help='glob pattern', nargs='+',
                   default=['*.rst', '*.txt', '*.md', '*.tex'])
    p.add_argument('--exclude', help='directories to exclude', nargs='+',
                   default=['.egg-info'])
    p.add_argument('-v', '--verbose', action='store_true')
    P = p.parse_args()

    try:
        findtext(P.rdir, P.glob, P.exclude, P.verbose)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
