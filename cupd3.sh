#!/bin/bash
for d in anaconda3 miniconda3
 do
 if [[ -d ~/$d ]]; then
   ~/$d/bin/conda install --yes matplotlib scipy numpy astropy pandas xlrd h5py scikit-image bokeh mkl python conda ipython ephem pip numba spyder
 fi
done
