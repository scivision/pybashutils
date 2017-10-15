#!/bin/bash

# consider Python dircmp, filecmp

[[ $# -ne 2 ]] && { echo "diffdir DIR1 DIR2"; exit 1; }

#compares directory trees by filename only -- only differences are reported

diff <(cd $1 && find 2>/dev/null | sort) <(cd $2 && find 2>/dev/null | sort)  
