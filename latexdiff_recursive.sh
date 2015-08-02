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

flist=$(ls $old/*.tex)


for f in ${flist[*]}; do
    b=$(basename $f)
    latexdiff $old/$b $new/$b > /tmp/$b
done

if [[ -n $main ]]; then
  (
    cd /tmp
    pdflatex $main
    bibtex $main
    pdflatex $main
    pdflatex $main
  )
fi