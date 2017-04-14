#!/usr/bin/env python
"""
iteratively find files with "bad" characters that Python doesn't like.
useful for f2py, BibTeX and more.
Michael Hirsch, Ph.D.
"""
from tempfile import mkstemp
from subprocess import run
from sys import stderr
from pathlib import Path

try:
    run('iconv -f utf-8 -t ascii <<< \ ',shell=True,executable='/bin/bash',timeout=0.5)
    fix=True
except Exception as e:
    fix=False

def scanbadchar(path,ext):
    """
    ext: file extension INCLUDING PERIOD
    """
    path = Path(path).expanduser()
    if path.is_file():
        flist = [path]
    elif path.is_dir():
        flist = path.glob('*'+ext)
    else:
        raise FileNotFoundError(f'{path} not found')

    for f in flist:
        try:
            f.open('r').read()
        except UnicodeDecodeError:
            print(f'BAD character in {f}',file=stderr)
            if fix:
                ofn = mkstemp(f.suffix)[1]
                print(f'{f} => {ofn}')
                # this returns stderr 1 if characters were bad despite conversino success.
                run(f'iconv -c -f utf-8 -t ascii {f} > '+ofn,shell=True,timeout=1)
                run(['diff',str(f),str(ofn)],timeout=1)
                print('---------------')

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('path',help='top path to search')
    p.add_argument('ext',help='file extension WITH PERIOD',nargs='?',default='')
    p = p.parse_args()

    scanbadchar(p.path,p.ext)
