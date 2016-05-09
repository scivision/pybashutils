#!/bin/bash

declare -a compilers=(gcc g++ gfortran)
declare -a vers=(4.8 4.9 5 6)

for g in "${compilers[@]}"; do
  i=1 #lower number, lower priority
  for v in "${vers[@]}"; do
    if [[ $($g-$v -dumpversion) ]]; then #is compiler installed
      update-alternatives --install /usr/bin/$g $g /usr/bin/$g-$v $i
      ((i++))
    fi
  done
done

