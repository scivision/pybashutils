#!/bin/bash
# pushes all git directories under $rdir with changes.
# Michael Hirsch
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

#    if [[ -s test/test.py ]]; then
#      nosetests -v test/test.py
#    fi

    if [[ -n $(git --no-pager diff HEAD 2>/dev/null) ]] || [[ -n $1 ]]; then
      git diff HEAD
      git commit -a && git push
    fi

    untrac=$(git ls-files -o -d --exclude-standard)
    if [[ -n $untrac ]]; then
        echo $untrac
        exit 1
    fi
  done
)
