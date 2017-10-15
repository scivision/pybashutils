#!/bin/bash
[[ $# == 0 ]] && { echo "Usage: eps2pdf input.eps"; exit 1; }
[[ $# > 2  ]] && { echo "Usage: eps2pdf input.eps"; exit 1; }
[[ $# == 1 ]] && OutFN=joined.pdf
[[ $# == 2 ]] && OutFN=$2
#[[ $# -eq 3 ]] && Orient=$3


gs -sDEVICE=pdfwrite \
   -dRotatePages=true \
   -dEPSFitPage \
   -dNOPAUSE -dBATCH -dSAFER \
   -sOutputFile=$OutFN \
   $1
#-dEPSFitPage
#-dAutoRotatePages=/PageByPage \ #didn't work for matlab eps
#   -c "<</Orientation 2>> setpagedevice" \ # didn't work
#    -c quit


echo "wrote $1 to $OutFN"
