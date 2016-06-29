#!/usr/bin/env python
"""
sets core.fileMode=false for git repos
mostly for Windows, particularly Cygwin
"""
from pythonutils.ChDir import ChDir
import os
from subprocess import call
#
from pythonutils.gitcommon import codepath

rdir = codepath()

print('setting fileMode=false for all directories under {}'.format(rdir))
dlist = [x for x in rdir.iterdir() if x.is_dir()]
for d in dlist:
    with ChDir(d):
        call(['git','config','core.filemode','false'])
