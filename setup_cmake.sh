#!/bin/bash
set -e

sudo apt install g++ make libncurses-dev

cver=3.10.2

wd=/tmp
wget -nc -P $wd https://cmake.org/files/v${cver:0:4}/cmake-$cver.tar.gz

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

make -j2

[[ `make install` ]] && sudo make install
)

echo "reopen a new terminal to use CMake $cver"

[[ -z $INSTALL_DIR ]] && echo " you may wish to add $INSTALL_DIR to your PATH"
