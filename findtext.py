#!/usr/bin/env python
import warnings
from pathlib import Path
import subprocess
from binaryornot.check import is_binary
import colorama
from typing import List, Union, Iterable

colorama.init()

MAXSIZE = 20e6  # [bytes]
EXT = ['*.py', '*.rst', '*.txt', '*.pdf',
       '*.md', '*.tex', '*.f', '*.f90', '*.for']


def findtext(root: Path, txt: str, globext: List[str], verbose: int):
    if isinstance(globext, (Path, str)):
        globext = [globext]

    for ext in globext:
        # in case "ext" is actually a specific filename
        e = Path(ext).expanduser()
        if e.is_file():
            searchlist([e], txt, verbose)
        else:  # usual case
            searchlist(Path(root).expanduser().rglob(str(e)), txt, verbose)


def searchlist(flist: Union[List[Path], Iterable], txt: str, verbose: int):

    mat = []

    endl = '\n' if verbose >= 0 else ' '

    for f in flist:
        # note that searchfile() does NOT work for PDF even with text inside...but Grep does. Hmm..
        if f.is_file() and f.stat().st_size < MAXSIZE:
            matchinglines = None

            if not is_binary(str(f)):
                here, matchinglines = searchfile(f, txt, verbose)
            elif f.suffix == '.pdf':
                here = searchbinary(f, txt)
            else:
                continue

            if here:
                print(colorama.Back.MAGENTA + str(f), end=endl)
                if matchinglines and verbose >= 0:
                    print(colorama.Back.BLACK + '\n'.join(matchinglines))
                mat.append(f)


def searchbinary(f: Path, txt: str) -> bool:
    # FIXME: use Python directly to make cross-platform Windows
    try:
        subprocess.check_call(['grep', txt, f],
                              stdout=subprocess.DEVNULL)  # grep return 0 if match
        return True
    except subprocess.CalledProcessError:  # grep returns 1 if no match
        return False
    except Exception as e:  # catch-all for unexpected error
        warnings.warn(f'{f}  {e}')

    return False


def searchfile(f: Path, txt: str, verbose: int):
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
            if verbose > 0:
                warnings.warn(f'{f} {e}')

    return here, matchinglines


if __name__ == '__main__':
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    from argparse import ArgumentParser
    p = ArgumentParser(
        description='searches for TEXT under DIR and echos back filenames')
    p.add_argument('txt', help='text to search for')  # required
    p.add_argument('globext', help='filename glob', nargs='?', default=EXT)
    p.add_argument('dir', help='root dir to search', nargs='?', default='.')
    p.add_argument('-v', '--verbose', action='store_true')
    p.add_argument('-q', '--quiet', action='store_true')
    P = p.parse_args()

    verbose = 0
    verbose -= P.quiet
    verbose += P.verbose

    findtext(P.dir, P.txt, P.globext, verbose)
