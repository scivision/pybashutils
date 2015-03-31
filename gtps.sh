#!/bin/bash

rdir=~/code/

for cdr in $(find $rdir -mindepth 1 -maxdepth 1 -type d); do
      
(cd $cdr; [[ -n `git diff HEAD` ]] 2>/dev/null && (echo "pushing $cdr"; git commit -a; git push; sleep 0.$[ ($RANDOM % 1000) ]))

done
