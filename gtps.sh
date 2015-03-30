#!/bin/bash

rdir=~/code/

for cdr in $(find $rdir -mindepth 1 -maxdepth 1 -type d); do
      echo "pushing $cdr"
      (cd "$cdr" && git commit -a; git push)
       sleep 0.$[ ($RANDOM % 1000)+0.2 ] #so as not to hammer the remote server$
done
