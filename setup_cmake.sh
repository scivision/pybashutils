#!/bin/bash
# requires libncurses-dev
set -e

cver=3.9.0

wd=/tmp
wget -nc -P $wd https://cmake.org/files/v${cver:0:3}/cmake-$cver.tar.gz

(
cd $wd

tar -xf cmake-$cver.tar.gz

if [[ $# -ge 1 ]]; then
    echo "installing cmake to $1"
    ./cmake-$cver/bootstrap --prefix=$1
else
    echo "installing cmake to default location"
    ./cmake-$cver/bootstrap
fi

make -j4

make install
)

echo "reopen a new terminal to use CMake $cver"

[[ -z $INSTALL_DIR ]] && echo " you may wish to add $INSTALL_DIR to your PATH"
