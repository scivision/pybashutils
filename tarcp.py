#!/usr/bin/env python
"""
tars (optional compression) and moves files per directory
"""
import logging
from pathlib import Path
import tarfile
from argparse import ArgumentParser


def tarcp(din, fout, method='xz', compresslevel=1):
    # %% io setup
    assert isinstance(method, str), 'xz bz2 gz or ""'
    din = Path(din).expanduser()
    assert din.is_dir(), 'must specify input directory'
# %% must have nested .tar suffix or some archivers don't understand file
    fout = Path(fout).expanduser().with_suffix('.tar.' + method)
    fout.parent.mkdir(parents=True, exist_ok=True)
# %% list ONLY 1st level subdirectories
    dlist = [d for d in din.iterdir() if d.is_dir()]
    print(f'Found {len(dlist)} directories in {din}  tarring to {fout}')
# %% main loop
    with tarfile.open(fout, mode="w:"+method, compresslevel=compresslevel) as tar:
        for d in dlist:
            try:
                tar.add(d, recursive=True)
            except PermissionError:
                logging.error(f'E: permission: {d}')

    assert fout.is_file(), f'something prevented {fout} from being created'


def main():
    p = ArgumentParser(description="tars (optional compression) and moves files per directory")
    p.add_argument('din', help='input directory to recursively tar')
    p.add_argument('fout', help='tar file to write including path')
    P = p.parse_args()

    tarcp(P.din, P.fout)


if __name__ == '__main__':
    main()
