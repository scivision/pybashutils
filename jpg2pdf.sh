#!/bin/bash
# converts directory of PNGs to PDF via globbing
convert -page letter -adjoin "$1*.jp*g" "$2joined.pdf"

