#!/bin/bash

if [[ $# -eq 0 ]]; then
 fDir="."
elif [[ $# -eq 1 ]]; then
 fDir=$1
else
 echo usage: "findvid [DIR]"
 exit 0
fi

find $fDir -regextype posix-egrep -type f -iregex '.*\.(avi|mov|mp4|mpg|mpeg|webm|ogv|mkv|wmv)$'
