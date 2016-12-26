#!/bin/bash

# requires libncurses-dev

(
cver=3.7.1

wd=$(mktemp -d)
wget -nc -P $wd https://cmake.org/files/v3.7/cmake-$cver.tar.gz
cd $wd
tar -xf cmake-$cver.tar.gz
./cmake-$cver/configure
make -j7
sudo make install
echo "reopen a new terminal to use CMake $cver"
)
