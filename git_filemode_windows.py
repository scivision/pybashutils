#!/usr/bin/env python
"""
sets core.fileMode=false for git repos
mostly for Windows, particularly Cygwin
"""
from pythonutils import Path
from pythonutils.ChDir import ChDir
from platform import system
import os
from subprocess import call

# autodetect root directory  c:\code or ~/code  arbitrary choice
plat = system().lower()
if plat.startswith('cygwin'): # assume /cygdrive/c, you're welcome to change
    rdir = Path(os.environ['SYSTEMDRIVE'])
else:
    rdir = Path.home() # windows, not Cygwin and all other OS

rdir = rdir / 'code'

print('setting fileMode=false for all directories under {}'.format(rdir))
dlist = [x for x in rdir.iterdir() if x.is_dir()]
for d in dlist:
    with ChDir(d):
        call(['git','config','core.filemode','false'])
