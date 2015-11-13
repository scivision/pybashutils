#!/usr/bin/env python3
"""
empty_file.py
makes empty file(s)
in bash you'd do  >myfile or touch myfile
"""
from __future__ import unicode_literals
from six import string_types,PY2
from pathlib2 import Path
if PY2: FileNotFoundError=IOError

def empty_file(flist):
    if isinstance(flist,(string_types,Path)):
        flist=[flist]

    for f in flist:
       touch(f)


def touch(f):
    f = Path(f).expanduser()

    try:
        f.write_text('')
    except FileNotFoundError:
        f.parent.mkdir(parents=True,exist_ok=True)
        f.write_text('')


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('dirs',help='directories to create',nargs='+',default='')
    p = p.parse_args()

    empty_file(p.dirs)
