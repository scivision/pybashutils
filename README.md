[![image](https://travis-ci.org/scivision/pybashutils.svg?branch=master)](https://travis-ci.org/scivision/pybashutils)

[![image](https://coveralls.io/repos/github/scivision/pybashutils/badge.svg?branch=master)](https://coveralls.io/github/scivision/pybashutils?branch=master)

[![Maintainability](https://api.codeclimate.com/v1/badges/530575d7d1a47e7f3fa1/maintainability)](https://codeclimate.com/github/scivision/pybashutils/maintainability)

Python-bash-matlab-octave-utils
===============================

Collection of Bash and Python scripts I've made that may be generally
useful

  function          description
  ----------------- -----------------------------------------------------------------------------
  h5tester.py       test HDF5 files for corruption--if the variable(s) have Fletcher 32 enabled
  cupd              update conda packages (well, the ones I use)
  checkIP           Sends you an email automatically if your IP address changes
  getIP.py          gets your public IP address (not the internal NAT address)
  findtext          find text inside files matching pattern.
  mx                mount network share example using SSHFS
  memfree.m         Estimates available RAM for Matlab/Octave under Windows, Mac, Linux
  checkRAM.m        check if a proposed N-D array with fit in available RAM (w/o swap)
  setup\_cmake.sh   setup latest CMake from source (without sudo)

Prereq
------

    apt install sshfs g++ libncurses-dev make

Install
-------

    python -m pip install -e .

Usage
-----

### SSHFS mount/unmount

1.  Mounting the "U" network drive at Boston University over SSHFS
    (slight modifications to the script allow using this anywhere)

one time setup:

    mkdir ~/U

2.  mount U drive to your PC, like "mounting a network drive" in
    Windows, here we assume the BU username is `jdoe`:

        mU jdoe

and your network drive is available as \~/U

3.  Unmounting the "U" drive. When done for the day, suggest unmounting
    in case to help mitigate security risks:

        uU

Note: if you have any files open (like say a spreadsheet on the `~/U`
drive), `~/U` will stay connected until you close that file(s).

### Get Public IP address

    getIP.py
