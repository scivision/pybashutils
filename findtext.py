#!/usr/bin/env python
r"""
Recursively find files containing text.
This method is slower than grep, but is cross-platform and easier syntax.

benchmarks:

time findtext xarray
18.6 sec

# note there are no "" on the command below. It's the equivalent of the defaults for the Python script.
time grep -r -l \
  --exclude-dir={\_site,\.git,\.eggs,build,dist,\.mypy_cache,.pytest_cache,*\.egg-info} \
  --include=*.{py,cfg,ini,txt,pdf,md,rst,tex,f,f90,for,f95,c,h,cpp,hpp,m} \
  xarray .
0.55 sec

---
time findtext xarray "*.py"
1.14 sec

time grep -r -l \
  --exclude-dir={\_site,\.git,\.eggs,build,dist,\.mypy_cache,.pytest_cache,*\.egg-info} \
  --include=*.py  xarray .
0.15 sec

"""
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
       '*.cmake',
       '*.f', '*.f90', '*.for', '*.f95',
       '*.c', '*.h', '*.cpp', '*.hpp',
       '*.m']
EXCLUDEDIR = ['_site', '.git', '.eggs', 'build', 'dist', '.mypy_cache', '.pytest_cache']


def findtext(root: Path, txt: str,
             globext: Union[str, Path, List[str]],
             exclude: List[str], verbose: bool):
    """
    multiple extensions with braces like Linux does not work in .rglob()
    """

    root = Path(root).expanduser()

    if isinstance(globext, (str, Path)):
        globext = [str(globext)]

    for ext in globext:
        searchlist(root.rglob(ext), txt, exclude, verbose)


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
    p = ArgumentParser(description='searches for TEXT under DIR and echos back filenames')
    p.add_argument('txt', help='text to search for')  # required
    p.add_argument('globext', help='filename glob', nargs='?', default=EXT)
    p.add_argument('dir', help='root dir to search', nargs='?', default='.')
    p.add_argument('-e', '--exclude', help='exclude files/dirs', nargs='+', default=EXCLUDEDIR)
    p.add_argument('-v', '--verbose', action='store_true')
    P = p.parse_args()

    findtext(P.dir, P.txt, P.globext, P.exclude, P.verbose)


if __name__ == '__main__':
    main()
