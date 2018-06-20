#!/usr/bin/env python
"""
recursively find video files based on extension.

"""
from pathlib import Path
import subprocess

PURE = True
# %%


def findvid(path: Path):
    """
    recursive file search in Pure Python.
    about 10 times slower than Linux find, but platform-independent.
    """
    ext = ['avi', 'mov', 'mp4', 'mpg', 'mpeg', 'webm', 'ogv', 'mkv', 'wmv']
    path = Path(path).expanduser()

    for e in ext:
        print(f'searching *.{e}\r', end="", flush=True)
        # need sorted() for "if not flist" to work.
        flist = sorted(path.glob(f'**/*.{e}'))
        if not flist:
            continue

        print('\n'.join(map(str, flist)))
# %% clear last line before returning
    print('\r                         \r', end="")


def findvid_linux(path: Path, verbose: bool=False):
    """
    recursive file search using GNU find
    """
    path = Path(path).expanduser()

    cmd = ['find', path, '-type', 'f',
           '-regextype', 'posix-egrep',
           '-iregex', '.*\.(avi|mov|mp4|mpg|mpeg|webm|ogv|mkv|wmv)$']

    if verbose:
        print(' '.join(cmd))

    ret = subprocess.run(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL,
                         universal_newlines=True)

    returncode = ret.returncode
    if returncode in (0, 1):
        pass
    elif returncode == 2:
        raise IOError('GNU find error or not found')
    else:
        raise IOError(returncode)

    vids = ret.stdout.split('\n')
    if vids:
        print('\n'.join(vids), end="")


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('path', help='root path to start recursive search',
                   nargs='?', default='.')
    p.add_argument('-v', '--verbose', action='store_true')
    p = p.parse_args()

    try:
        findvid_linux(p.path, p.verbose)
    except IOError:
        findvid(p.path)
