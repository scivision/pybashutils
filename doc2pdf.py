#!/usr/bin/env python
"""
convert DOC, DOCX, RTF, etc. to PDF using LibreOffice
It leaves the original files alone, putting the PDF in the same directory.
"""
from pathlib import Path
from argparse import ArgumentParser
import subprocess


def main():
    p = ArgumentParser()
    p.add_argument('path', help='path to work in')
    p.add_argument('-g', '--glob', help='file extensions to convert', nargs='+',
                   default=['*.doc', '*.docx', '*.rtf'])
    p = p.parse_args()

    path = Path(p.path).expanduser().resolve()

    for g in p.glob:
        for fn in path.glob(g):
            if fn.with_suffix('.pdf').is_file():
                continue

            print('')

            cmd = ['soffice', '--headless',
                   '--convert-to', 'pdf', str(fn)]

            subprocess.check_call(cmd, cwd=path)


if __name__ == '__main__':
    main()
