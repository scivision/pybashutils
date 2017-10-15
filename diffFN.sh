#!/bin/bash
#Michael Hirsch
#
# compares directory filenames, based on filename only--ignores file contents
#   since some systems don't have "tree"
# handles spaces in filenames
# a lot faster than checking file contents, as a preliminary check of 
#   massive file systems
#
# must specify full path: NOT ~ or $HOME
# EXAMPLE
# diffFN /home/me/dir1 /home/me/dir2

[[ $# -ne 2 ]] && { echo "diffFN DIR1 DIR2"; exit 1; }

#remove single trailing slash, if present
d1=${1%/}
d2=${2%/}

#count files, removing root directory name, sorting to keep out false differences
dir1list=($(find $d1 -type f 2>/dev/null | sed "s,^${d1}/,," | sort))
dir2list=($(find $d2 -type f 2>/dev/null | sed "s,^${d2}/,," | sort))

echo "${#dir1list[@]} files in $d1"
echo "${#dir2list[@]} files in $d2"

#make each element of sorted array appear on its own line
diff <(printf "%s\n" "${dir1list[@]}") <(printf "%s\n" "${dir2list[@]}")
