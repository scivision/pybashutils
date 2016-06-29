#!/usr/bin/env python
from platform import system
import os
from . import Path

def codepath():
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('codepath',help='path to code root',nargs='?')
    p = p.parse_args()

    if p.codepath:
        rdir = Path(p.codepath)
    else:
        # autodetect root directory  c:\code or ~/code  arbitrary choice
        plat = system().lower()
        if plat.startswith('cygwin'): # assume /cygdrive/c, you're welcome to change
            rdir = Path(os.environ['SYSTEMDRIVE'])
        else:
            rdir = Path.home() # windows, not Cygwin and all other OS

        rdir = rdir / 'code'

    return rdir
