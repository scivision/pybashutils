#!/usr/bin/env python
"""
tars (optional compression) and moves files per directory
"""
import logging
from pathlib import Path
import tarfile


def tarcp(din, fout, method='xz', compresslevel=1):
    # %% io setup
    assert isinstance(method, str), 'xz bz2 gz or ""'
    din = Path(din).expanduser()
    assert din.is_dir(), 'must specify input directory'
    # must have nested .tar suffix or some archivers don't understand file
    fout = Path(fout).expanduser().with_suffix('.tar.' + method)
    fout.parent.mkdir(parents=True, exist_ok=True)
# %% list ONLY 1st level subdirectories
    dlist = [d for d in din.iterdir() if d.is_dir()]
    print('Found {} directories in {}  tarring to {}'.format(len(dlist), din, fout))
# %% main loop
    with tarfile.open(str(fout), mode="w:"+method, compresslevel=compresslevel) as tar:
        for d in dlist:
            try:
                tar.add(str(d), recursive=True)
            except PermissionError:
                logging.error('E: permission: {}'.format(d))

    assert fout.is_file(), 'something prevented {} from being created'.format(fout)


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(
        description="tars (optional compression) and moves files per directory")
    p.add_argument('din', help='input directory to recursively tar')
    p.add_argument('fout', help='tar file to write including path')
    P = p.parse_args()

    tarcp(P.din, P.fout)
