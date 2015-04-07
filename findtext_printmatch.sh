#!/bin/bash

maxFileSize=10M  #don't search inside huge binary files

case $# in
1)
srchText=$1
fDir="."
fntmp="*" ;;
2)
fDir="."
srchText=$1
fntmp=$2 ;;
3)
fDir=$1
srchText=$2
fntmp=$3 ;;
*)
echo usage: "findtext [DIR] TEXT [FILENAME]"
echo searches for TEXT under DIR and echos back filenames
exit ;;
esac

# dont use -execdir, or you wont see which directory the found files are in!
find $fDir -type f -name "$fntmp" -size -$maxFileSize \
    -exec grep --ignore-case "$srchText" {} +
