#!/bin/bash 
# count number of times script forked  
# http://stackoverflow.com/questions/17718508/how-to-count-number-of-forked-sub-processes


fork=0
set -o monitor
trap "((++fork))" CHLD


X=10
for i in $(seq 1 $X); do           #fastest way, forks onces
#for i in $(eval echo {1..$X}); do #medium speed, forks once
#for ((i=1;i<=$X;i++));do          #slowest way, does not fork
: #no-op
done


echo "this script forked  $fork  times"

