#!/bin/bash


old=$1
new=$2

flist=$(ls $old/*.tex)


for f in ${flist[*]}; do
    b=$(basename $f)
    latexdiff $old/$b $new/$b > /tmp/$b
done

