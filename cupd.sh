#!/bin/bash
for d in anaconda miniconda
 do
 if [[ -d ~/$d ]]; then
~/$d/bin/conda update matplotlib scipy numpy astropy pandas xlrd h5py scikit-image opencv bokeh mkl python conda ipython ephem pip numba spyder
 fi
done