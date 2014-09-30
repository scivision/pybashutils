#!/bin/bash
# converts directory of PNGs to PDF via globbing
convert -page letter -adjoin "$1*.png" "$2joined.pdf"

