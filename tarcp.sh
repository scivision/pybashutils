#!/bin/bash
# Michael Hirsch
# tars (w/o compressing) and moves files per directory

: ${2?example: tarcp ~/inDir /media/outDir}

MainDir=$1
OutDir=$2

#check if OutDir directory already exists
TarOutDir=$OutDir/$MainDir #not for use inside tar command
[[ ! -d $TarOutDir ]] && { echo creating $TarOutDir; mkdir $TarOutDir; }

#list ONLY 1st level subdirectories
DirList=($(find "$MainDir" -maxdepth 1 -mindepth 1 -type d | sort))

#main loop
for currDir in "${DirList[@]}"; do
currTarOut="$OutDir/$currDir.tar"
echo "tarring $currDir to $currTarOut"
tar --recursion --create --file="$currTarOut" --directory="$currDir" .

# below would probably be better for 100,000 files per directory since {} + acts like xargs 
# UPDATE: I have tried code below and it is no faster than tar itself
#find "$currDir" -type f -name "*" \
#        -execdir tar --append --file="$currTarOut" --directory="$currDir" {} +

done

echo "extract with tar xvf --strip-components *.tar to get rid of . dot directories"
