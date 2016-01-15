#!/bin/bash

pat=$1
[[ -z $pat ]] && { echo "must specify a file pattern to process"; exit 1; }

for f in $(ls -A $pat); do
#g=$(echo $f | sed -e 's/\.//') #removes first (leftmost) dot in filename. FFMPEG can handle only one dot in filename.
g=$(echo $f | sed -e 's/\:/-/g') #removes all colons in filename, which FFMPEG can't handle
#echo $g
mv -iv $f $g
done
