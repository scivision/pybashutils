#!/bin/bash

# requires libncurses-dev
set -e

(
cver=3.8.1

wd=$(mktemp -d)
wget -nc -P $wd https://cmake.org/files/v${cver:0:3}/cmake-$cver.tar.gz
cd $wd
tar -xf cmake-$cver.tar.gz
./cmake-$cver/configure
make -j4
sudo make install
echo "reopen a new terminal to use CMake $cver"
)
