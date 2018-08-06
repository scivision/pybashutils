#!/usr/bin/env python
"""
useful for updating templates.

e.g.

meld_all .appveyor.yml

meld_all .appveyor.yml -l Fortran
"""
from pathlib import Path
from argparse import ArgumentParser
import filecmp
import logging
import subprocess
try:
    import ghlinguist as ghl
except ImportError:
    ghl = None

EXE = 'meld'


def meldloop(root: Path, filename: Path, language: str=None, exe: str=EXE, strict: bool=False):
    assert root.is_dir(), f'{root} is not a directory'
    assert filename.is_file()
    
    flist = list(root.rglob(filename.name))
    
    si = 1 if strict else 2
    
    if language is None:
        language = ghl.linguist(filename.parent, rtype=True)

    print(f'comparing {len(flist)} files vs {filename} {language}')

    # Not using check_call due to spurious errors
    for f in flist:
        if filecmp.cmp(f, filename, shallow=False):
            print(f'SAME: {f.parent}')
            continue

        if ghl is not None:
            langlist = ghl.linguist(f.parent)
            if langlist is None:
                logging.warning(f'SKIP: {f.parent}')
                continue

            thislangs = [l[0] for l in langlist[:si]]
            if language not in thislangs:
                print(f'SKIP: {f.parent} {thislangs}')
                continue

        subprocess.run([exe, str(filename), str(f)])


def main():
    p = ArgumentParser()
    p.add_argument('filename', help='filename to compare against')
    p.add_argument('root', help='top-level directory to search under', nargs='?')
    p.add_argument('-l', '--language', help='language to template')
    p.add_argument('-exe', help='program to compare with', default=EXE)
    p.add_argument('-s', '--strict', help='compare only with first language match', action='store_true')
    p = p.parse_args()

    fn = Path(p.filename).expanduser()
    if not fn.is_file():
        raise FileNotFoundError(f'{fn} is not a file')

    root = fn.resolve().parents[1] if not p.root else Path(p.root).expanduser()
    if not root.is_dir():
        raise FileNotFoundError(f'{root} is not a directory')

    meldloop(root, fn, p.language, p.exe, strict=p.strict)


if __name__ == '__main__':
    main()
