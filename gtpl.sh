#!/bin/bash
# for a root directory $rdir, assumes all subdirectories are Git repos
# and pulls to the current branch

case "$(uname -s)" in
    CYGWIN*) hd=$SYSTEMDRIVE;  ;;
    *)       hd=$HOME; ;;
esac


rdir=$hd/code

for cdr in $(find $rdir -mindepth 1 -maxdepth 1 -type d); do
       echo "pulling $cdr"
       (cd "$cdr" && exec git pull)
       sleep 0.$[ ($RANDOM % 1000) ] #so as not to hammer the remote server, delay of 0-1 second
done
