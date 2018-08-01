#!/usr/bin/env python
import logging
from pathlib import Path
import subprocess
from binaryornot.check import is_binary
from typing import List, Union, Iterable, Tuple
from argparse import ArgumentParser
try:
    import colorama
    MAGENTA = colorama.Back.MAGENTA
    BLACK = colorama.Back.BLACK
    colorama.init()
except ImportError:
    MAGENTA = BLACK = ''

MAXSIZE = 20e6  # [bytes]
EXT = ['*.py', '*.cfg', '*.ini',
       '*.txt', '*.pdf',
       '*.md', '*.rst',
       '*.tex',
       '*.f', '*.f90', '*.for', '*.f95',
       '*.c', '*.h', '*.cpp', '*.hpp',
       '*.m']


def findtext(root: Path, txt: str, globext: List[str], exclude: List[str], verbose: bool):
    if isinstance(globext, (Path, str)):
        globext = [globext]

    root = Path(root).expanduser()

    for ext in globext:
        # in case "ext" is actually a specific filename
        e = Path(ext).expanduser()
        if not e.name.startswith('*') and e.is_file():
            searchlist([e], txt, exclude, verbose)
        else:  # usual case
            searchlist(root.rglob(str(e)), txt, exclude, verbose)


def searchlist(flist: Union[List[Path], Iterable], txt: str, exclude: List[str], verbose: bool):

    mat = []
    exc = set(exclude)

    for f in flist:
        if exc.intersection(set(str(f.resolve()).split('/'))):
            continue
        # note that searchfile() does NOT work for PDF even with text inside...but Grep does. Hmm..
        if f.is_file() and f.stat().st_size < MAXSIZE:
            matchinglines: List[str] = []

            if not is_binary(str(f)):
                here, matchinglines = searchfile(f, txt)
            elif f.suffix == '.pdf':
                here = searchbinary(f, txt)
            else:
                logging.info(f'skipped {f}')
                continue

            if here:
                mat.append(f)
                if verbose:
                    print(MAGENTA + str(f))
                    print(BLACK + '\n'.join(matchinglines))
                else:
                    print(f)


def searchbinary(f: Path, txt: str) -> bool:
    # FIXME: use Python directly to make cross-platform Windows
    try:
        subprocess.check_call(['grep', txt, f],
                              stdout=subprocess.DEVNULL)  # grep return 0 if match
        return True
    except subprocess.CalledProcessError:  # grep returns 1 if no match
        return False
    except Exception as e:  # catch-all for unexpected error
        logging.warning(f'{f}  {e}')

    return False


def searchfile(f: Path, txt: str) -> Tuple[bool, List[str]]:
    here = False
    matchinglines = []
    """
    NO speedup observed from doing this first
    if not txt in str(f):
       return here,matchinglines
    """

    with f.open('r') as o:
        try:
            for i, l in enumerate(o):
                if txt not in l:
                    continue
                matchinglines.append(f'{i}: {l}')
                here = True
        except UnicodeDecodeError as e:
            logging.info(f'{f} {e}')

    return here, matchinglines


def main():
    p = ArgumentParser(
        description='searches for TEXT under DIR and echos back filenames')
    p.add_argument('txt', help='text to search for')  # required
    p.add_argument('globext', help='filename glob', nargs='?', default=EXT)
    p.add_argument('dir', help='root dir to search', nargs='?', default='.')
    p.add_argument('-e', '--exclude', help='exclude files/dirs', nargs='+', default=('.eggs', 'build/'))
    p.add_argument('-v', '--verbose', action='store_true')
    P = p.parse_args()

    findtext(P.dir, P.txt, P.globext, P.exclude, P.verbose)


if __name__ == '__main__':
    main()
