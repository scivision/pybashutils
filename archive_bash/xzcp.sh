#!/bin/bash
# Michael Hirsch
# tars, XZ, and moves files per directory
: ${2?example: tarcp ~/inDir /media/outDir}

MainDir=$1
OutDir=$2

mkdir -p $OutDir

#list ONLY 1st level subdirectories
dlist=($(find "$MainDir" -maxdepth 1 -mindepth 1 -type d | sort))
echo "Found directories: ${dlist[*]}"

#main loop
for din in "${dlist[@]}"; do
    cout="$OutDir/$din.tar.xz"
    echo "tarring $din to $cout"
    XZ_OPT=-0 tar cJf "$cout" "$din"
done

echo "extract with tar xvf --strip-components=1 *.tar to get rid of . dot directories"

# below (actually wasn't) better for 100,000 files per directory since {} + acts like xargs 
# UPDATE: I have tried code below and it is no faster than tar itself
#find "$currDir" -type f -name "*" \
#        -execdir tar --append --file="$currTarOut" --directory="$currDir" {} +
