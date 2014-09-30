#!/bin/bash
# uses Ghostscript to convert PDF to PNG at good quality
# Michael Hirsch

echo "if you're trying to extract images, use pdfimages program instead"
inpdf=$1
firstpg=$2
lastpg=$3
dpi=300 #user specified

#basestem=$(basename $inpdf .pdf) #no directory
instem=${inpdf%.*} #no $ on inpdf

gs -r$dpi -dSAFER -dBATCH -dNOPAUSE -sDEVICE=png16m \
	-dFirstPage=$firstpg -dLastPage=$lastpg \
	-sOutputFile="$instem.png" "$inpdf"
