#!/bin/bash
# Michael Hirsch 2013
# 7zip's files to a directory

: ${2?example: 7zcp ~/inDir /media/outDir}

MainDir=$1
OutDir=$2

mkdir -p $OutDir

#list ONLY 1st level subdirectories
dlist=($(find "$MainDir" -maxdepth 1 -mindepth 1 -type d | sort))
echo "Found directories: ${dlist[*]}"

#main loop
for din in ${dlist[*]}; do
cout="$OutDir/$(basename $din).7z"

# no clobber
[[ -a $cout ]] && { echo "Skipping $din"; continue; }

echo "7zipping and moving $din to $cout"

# don't use the -o option, it doesn't seem to work right
7z a -t7z -mx=3 -mmt=on -m0=lzma2 "$cout" "$din"

done
