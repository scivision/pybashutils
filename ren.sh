#!/bin/bash

for f in $(ls *.png); do
#g=$(echo $f | sed -e 's/\.//') #removes first (leftmost) dot in filename. FFMPEG can handle only one dot in filename.
g=$(echo $f | sed -e 's/\:/-/g') #removes all colons in filename, which FFMPEG can't handle
#echo $g
mv -iv $f $g
done
