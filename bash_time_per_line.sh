#!/bin/bash -x
# monitor time for each line of script (needs #!/bin/bash -x)
# http://stackoverflow.com/questions/4336035/performance-profiling-tools-for-shell-scripts

PS4='$(date "+%s.%N ($LINENO) + ")'

X=10
for i in $(seq 1 $X); do           #fastest way, forks onces
#for i in $(eval echo {1..$X}); do #medium speed, forks once
#for ((i=1;i<=$X;i++));do          #slowest way, does not fork
: #no-op
done

