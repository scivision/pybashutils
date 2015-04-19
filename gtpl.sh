#!/bin/bash
# for a root directory $rdir, assumes all subdirectories are Git repos
# and pulls to the current branch

case "$(uname -s)" in
    CYGWIN*) hd=$SYSTEMDRIVE;  ;;
    *)       hd=$HOME; ;;
esac


rdir=$hd/code
ldir=$(find -H $rdir -mindepth 1 -maxdepth 1 -type d)
#echo "pulling ${ldir[@]}"
(
  for cdr in ${ldir[@]}; do
     cd "$cdr" && git pull || echo "ERROR pulling $cdr"
     sleep 0.$[ ($RANDOM % 1000) ] #so as not to hammer the remote server, delay of 0-1 second
  done
)
