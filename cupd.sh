#!/bin/bash
# designed to work in Linux and Windows(Cygwin). Should(!) work on Mac, if not let me know.
# assumes install directory:
#   Windows: c:\Anaconda
#   Linux/Mac: ~/anaconda
# I use this to keep lots of PCs in my GNU Parallel HPCC updated with the same Python modules.
# if you don't like this auto-install behavior, change "install --yes" to "update --yes"
# Michael Hirsch

set +e

#detect operating system
case "$(uname -s)" in
    CYGWIN*) hd=$SYSTEMDRIVE; sd=Scripts ;;
    *)       hd=$HOME; sd=bin ;;
esac

for d in anaconda anaconda2 miniconda miniconda2 anaconda3 miniconda3
 do
 if [[ -d $hd/$d ]]; then
  cdir=$hd/$d/$sd
  $cdir/conda install --yes matplotlib seaborn scipy numpy astropy pandas xlrd h5py scikit-image bokeh python conda ipython ephem pip numba spyder ipython-notebook paramiko basemap jedi pylint netcdf4 requests #mkl
  $cdir/pip install --upgrade plotly
  $cdir/pip install --upgrade tifffile
  $cdir/pip install --upgrade oct2py spectral spacepy

  if [[ "${d: -1}" -ne 3 ]]; then #python 2.7
    $cdir/pip install --upgrade xray bottleneck cyordereddict
    $cdir/pip install --upgrade pydap #python 2.7
  fi
 fi
done
