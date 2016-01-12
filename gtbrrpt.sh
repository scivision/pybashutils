#!/bin/bash

case "$(uname -s)" in
    CYGWIN*) hd=$SYSTEMDRIVE;  ;;
    *)       hd=$HOME; ;;
esac


rdir=$hd/code
ldir=$(find -H $rdir -mindepth 1 -maxdepth 1 -type d)

(
  for cdr in ${ldir[@]}; do
    cd $cdr

    cb=$(git rev-parse --abbrev-ref HEAD)

    if [[ $cb != "master" ]]; then
        echo $cdr $cb
    fi
  done
)

