#!/bin/bash
#
# The quoted variables allow using backticks and other "nasty" characters in sed.
#
# usage:
# ./recursive_sed.sh  pathtofiles yuck yay
#
# References:
# https://stackoverflow.com/a/1585810
# https://unix.stackexchange.com/a/128758

set -e
set -u

path=$1
old=$2
new=$3

echo "${old} => ${new}"

find $path -not -path '*/\.git*' -type f -exec sed -i 's/'"${old}"'/'"${new}"'/g' {} +