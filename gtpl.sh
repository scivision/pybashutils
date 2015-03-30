#!/bin/bash
# for a root directory $rdir, assumes all subdirectories are Git repos
# and pulls to the current branch

rdir=~/code/

for cdr in $(find $rdir -mindepth 1 -maxdepth 1 -type d); do
       echo "pulling $cdr"
       (cd "$cdr" && exec git pull)
done
