#!/bin/bash
# Runs latexdiff on every file in a directory
#
# Cygwin prereqs: 
# texlive-collection-bibtexextra texlive-collection-binextra perl
#
# Michael Hirsch

old=$1
new=$2
main=$3 #optional for compilation

flist=$(find -H $old -maxdepth 1 -type f -name "*.tex")


for f in ${flist[*]}; do
    b=${f##*/}   #$(basename $f)
    latexdiff $old/$b $new/$b > /tmp/$b
done

echo "output to /tmp"

if [[ -n $main ]]; then
  (
    cd /tmp
    pdflatex $main
    bibtex $main
    pdflatex $main
    pdflatex $main
  )
fi
