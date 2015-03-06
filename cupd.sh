#!/bin/bash

#detect operating system
case "$(uname -s)" in
    CYGWIN*) hd=$SYSTEMDRIVE; sd=Scripts ;;
    *)       hd=$HOME; sd=bin ;;
esac

for d in anaconda miniconda anaconda3 miniconda3
 do
 if [[ -d $hd/$d ]]; then
  $hd/$d/$sd/conda install --yes matplotlib scipy numpy astropy pandas xlrd h5py scikit-image bokeh mkl python conda ipython ephem pip numba spyder
  # now let's try opencv, which isn't always available
   if $hd/$d/$sd/conda install --yes opencv; then :
   fi 

 fi
done
