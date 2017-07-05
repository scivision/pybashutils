#!/bin/bash

# requires libncurses-dev
set -e

INSTALL_DIR=$1

(
cver=3.9.0-rc5

wd=/tmp

wget -nc -P $wd https://cmake.org/files/v${cver:0:3}/cmake-$cver.tar.gz

cd $wd

tar -xf cmake-$cver.tar.gz

./cmake-$cver/bootstrap --prefix=INSTALL_DIR

make -j4

make install

echo "reopen a new terminal to use CMake $cver"

[[ -z $INSTALL_DIR ]] && echo " you may wish to add $INSTALL_DIR to your PATH"
)
