#!/bin/bash

if [[ $# -eq 0 ]]; then
 fDir="."
elif [[ $# -eq 1 ]]; then
 fDir=$1
else
 echo usage: "findvid [DIR]"
 exit 0
fi

#FIXME doesn't actually check to see that result is a valid video and not just a
#       PNG with the .avi extension

find $fDir -regextype posix-egrep -type f -iregex '.*\.(avi|mov|mp4|mpg|mpeg|webm|ogv|mkv|wmv)$' 2>/dev/null
