#!/usr/bin/env python
"""
iteratively find files with "bad" characters that Python doesn't like.
useful for f2py, BibTeX and more.
Michael Hirsch, Ph.D.
"""
import logging
import subprocess
from pathlib import Path

try:
    subprocess.check_call(['iconv', '--version'])
    FIX = True
except Exception as e:
    FIX = False


def scanbadchar(path, ext):
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
            logging.warning(f'BAD character in {f}')
            if FIX:
                print(f'fixing {f} ')
                # this returns stderr 1 if characters were bad despite conversion success.
                ret = subprocess.check_output(['iconv', '-c', '-f', 'utf-8', '-t', 'ascii', str(f)],
                                              timeout=5, universal_newlines=True)
                f.write_text(ret)


if __name__ == '__main__':
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('path', help='top path to search')
    p.add_argument('ext', help='file extension WITH PERIOD',
                   nargs='?', default='')
    p = p.parse_args()

    scanbadchar(p.path, p.ext)
