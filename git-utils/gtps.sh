#!/bin/bash
# pushes all git directories under $rdir with changes.
#
# PREREQ: for this to work properly, you must one-time type
# git config --global core.pager 'less -+F'
#
# Notes:
# if git commit is aborted (empty commit), it returns stderr 1 and git push doesn't execute


case "$(uname -s)" in
    CYGWIN*) hd=$SYSTEMDRIVE;  ;;
    *)       hd=$HOME; ;;
esac


rdir=$hd/code
ldir=$(find -H $rdir -mindepth 1 -maxdepth 1 -type d)

(
  for cdr in ${ldir[@]}; do
    cd $cdr
     echo -e "\n ---> $cdr"

#    if [[ -s tests/test.py ]]; then
#      nosetests -v test/test.py
#    fi

    if [[ -n $(git --no-pager diff HEAD 2>/dev/null) ]]; then
      git diff HEAD
      git commit -a && git push
    elif [[ -n $1 ]]; then
      git commit -a
      git push
    elif [[ -n $(git log --branches --not --remotes) ]]; then
      git log --branches --not --remotes && git push
    fi

    untrac=$(git ls-files -o -d --exclude-standard)
    if [[ -n $untrac ]]; then
        echo $untrac
        exit 1
    fi
  done
)
