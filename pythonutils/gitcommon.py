#!/usr/bin/env python
from platform import system
from . import Path

def codepath():
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('codepath',help='path to code root',nargs='?')
    p = p.parse_args()

    if p.codepath:
        rdir = Path(codepath)
    else:
        # autodetect root directory  c:\code or ~/code  arbitrary choice
        plat = system().lower()
        if plat.startswith('cygwin'): # assume /cygdrive/c, you're welcome to change
            rdir = Path(os.environ['SYSTEMDRIVE'])
        else:
            rdir = Path.home() # windows, not Cygwin and all other OS

        rdir = rdir / 'code'

        if not rdir.is_dir() and plat.startswith('linux'): #windows subsystem for Linux
            rdir = Path('/mnt/c/code')

    return rdir