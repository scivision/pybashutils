#!/bin/bash
# pushes all git directories under $rdir with changes.
# Michael Hirsch

case "$(uname -s)" in
    CYGWIN*) hd=$SYSTEMDRIVE;  ;;
    *)       hd=$HOME; ;;
esac


rdir=$hd/code
ldir=$(find -H $rdir -mindepth 1 -maxdepth 1 -type d)

for cdr in ${ldir[@]}; do
  if [[ -n `git --no-pager diff HEAD 2>/dev/null` ]]; then
    (cd $cdr && git diff HEAD && git commit -a && git push)
    sleep 0.$[ ($RANDOM % 1000)]
  fi
done
