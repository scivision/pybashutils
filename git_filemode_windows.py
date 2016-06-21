#!/usr/bin/env python
"""
sets core.fileMode=false for git repos
mostly for Windows, particularly Cygwin
"""
from pythonutils import Path
from platform import system
import os
from subprocess import call

class ChDir(object):
    """
    context manager for changing directories
    from https://pythonadventures.wordpress.com/2013/12/15/chdir-a-context-manager-for-switching-working-directories/
    Step into a directory temporarily.
    """
    def __init__(self, path):
        self.old_dir = os.getcwd()
        self.new_dir = path

    def __enter__(self):
        os.chdir(str(self.new_dir))

    def __exit__(self, *args):
        os.chdir(str(self.old_dir))

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
