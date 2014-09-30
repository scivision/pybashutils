#!/bin/bash
# converts non-text PDF with OCR
# Michael Hirsch 2014

# BUGS: won't work right if operating in parallel with two exactly the same filename stems

InputPDF="$1"

#get number of pages
nPages=$(pdftk $InputPDF dump_data | grep NumberOfPages | cut -d" " -f2)
echo "$nPages pages found in $InputPDF"

baseStem=$(basename $InputPDF .pdf) #no directory
tf=/dev/shm/tess_$baseStem # making it ready for GNU parallel

inStem=${InputPDF%.*} #no $ before InputPDF
outFN="$inStem-OCR.txt"

# if existing OCR file, move it aside
[[ -f $outFN ]] && mv -v $outFN $outFN-$(date -r $outFN '+%FT%T').txt

for (( i=1; i<=$nPages; i++ )); do
  echo "OCR page $i / $nPages into $outFN"
  # convert $InputPDF[$i] -resize 1000% -monochrome -density 2400 $tf #terrible tif
#  convert $InputPDF[$i] -geometry 8000x  $tf #png #better but not great
  pdftoppm -f $i -l $i -r 600 -gray -singlefile $InputPDF $tf #wonderful
  tesseract $tf.pgm "$tf" |& grep -v "Tesseract Open Source OCR Engine v"  #suppress welcome msg
  #now append to output file
  echo "---- Page $i / $nPages  (OCR) ----" >> "$outFN"
  cat "$tf.txt" >> "$outFN"
done

rm -v $tf.*
