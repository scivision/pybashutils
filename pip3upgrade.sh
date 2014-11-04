#!/bin/bash
# Keeping packages up to do -- at your own risk
#sudo apt-get install libblas-dev libatlas-dev libpng-dev python3-dev python-dev dvipng texlive-latex-base \
# libfreetype6-dev tk-dev libffi-dev liblapack-dev libhdf5-dev cmake libqt4-dev \
# python-tk python3-tk

#pyside is too enormous to bother with in pip

pkgs="cython cairocffi numpy six matplotlib scipy oct2py h5py pandas astropy sphinx pyflakes pylint sympy pep8 spyder moviepy ipython[notebook] pyserial pyephem scikit-image"
p="$pkgs rope_py3k"
sudo pip3 install --upgrade $p
p="$pkgs rope"
sudo pip install --upgrade $p
