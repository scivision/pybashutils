#!/usr/bin/env python
"""
sets core.fileMode=false for git repos
mostly for Windows, particularly Cygwin
"""
from pythonutils.ChDir import ChDir
import os
import sys
from time import sleep
from subprocess import run
#
from pythonutils.gitcommon import codepath

rdir = codepath()

print('git push for all directories under {}'.format(rdir))
dlist = [x for x in rdir.iterdir() if x.is_dir()]
for d in dlist:
    with ChDir(d):
        ret = run(['git','--no-pager','diff','HEAD'])

    if ret.stdout is None:
        print('{} no change'.format(d))
    else:
        sleep(5)
        sys.exit()




# if [[ -n $(git --no-pager diff HEAD 2>/dev/null) ]]; then
  # git diff HEAD
  # git commit -a && git push
# elif [[ -n $1 ]]; then
  # git commit -a
  # git push
# elif [[ -n $(git log --branches --not --remotes) ]]; then
  # git log --branches --not --remotes && git push
# fi

# untrac=$(git ls-files -o -d --exclude-standard)
# if [[ -n $untrac ]]; then
    # echo $untrac
    # exit 1
# fi