#!/bin/bash
# for a root directory $rdir, assumes all subdirectories are Git repos
# and pulls to the current branch

rdir=~/code/

for cdr in $(find $rdir -mindepth 1 -maxdepth 1 -type d); do
       echo "pulling $cdr"
       (cd "$cdr" && exec git pull)
       sleep 0.$[ ($RANDOM % 1000)+0.2 ] #so as not to hammer the remote server, delay of 0.2-1.2 second
done
