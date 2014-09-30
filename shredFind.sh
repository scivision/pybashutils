#!/bin/bash
# shreds files and subdirectories

: ${1?example: shredFind ~/shredDirAndSubDir ntimes}

MainDir=$1
if [ $# -gt 1 ]; then nTimes=$2; else nTimes=3; fi

#list ONLY subdirectories (not invocation directory itself)
DirList=($(find "$MainDir" -mindepth 1 -type d | sort))
nDir=${#DirList[@]};
nDir1=$(($nDir - 1))

#main loop
for i in $(seq 0 1 $nDir1); do
#currDirIn="$(readlink -f ${DirList[$i]})/"
currDirIn="${DirList[$i]}"
echo "shredding $currDirIn"
find "$currDirIn" -type f -name "*" \
        -execdir shred --verbose --iterations=$nTimes {} +
#	-execdir echo {} + #for testing
done

