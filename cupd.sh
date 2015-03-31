#!/bin/bash
# designed to work in Linux and Windows(Cygwin). Should(!) work on Mac, if not let me know.
# assumes install directory:
#   Windows: c:\Anaconda
#   Linux/Mac: ~/anaconda
# I use this to keep lots of PCs in my GNU Parallel HPCC updated with the same Python modules.
# if you don't like this auto-install behavior, change "install --yes" to "update --yes"
# Michael Hirsch

#detect operating system
case "$(uname -s)" in
    CYGWIN*) hd=$SYSTEMDRIVE; sd=Scripts ;;
    *)       hd=$HOME; sd=bin ;;
esac

for d in anaconda miniconda anaconda3 miniconda3
 do
 if [[ -d $hd/$d ]]; then
  cdir=$hd/$d/$sd
  $cdir/conda install --yes matplotlib seaborn scipy numpy astropy pandas xlrd h5py scikit-image bokeh python conda ipython ephem pip numba spyder ipython-notebook paramiko basemap jedi #mkl
  $cdir/pip install --upgrade tifffile oct2py
  # if $cdir/conda install --yes opencv; then :
  # fi

 fi
done
