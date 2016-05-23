.. image:: https://travis-ci.org/scienceopen/pybashutils.svg?branch=master
    :target: https://travis-ci.org/scienceopen/pybashutils

==========
bash-utils
==========
Collection of Bash/Python/Matlab/Octave scripts I've made that may be generally useful

=========   ===========
function    description
=========   ===========
cupd        update conda packages (well, the ones I use)
checkIP     Sends you an email automatically if your IP address changes
getIP       gets your public IP address (not the internal NAT address)
findtext    find text inside files matching pattern.
mx          mount network share example using SSHFS
memfree.m   Estimates available RAM for Matlab/Octave under Windows, Mac, Linux
checkRAM.m  check if a proposed N-D array with fit in available RAM (w/o swap)
=========   ===========



Installation:
-------------
This procedure assumes you're on a Linux device

1. download the code::

    cd ~
    git clone --depth 1 https://github.com/scienceopen/pybashutils.git

2. add the scripts to your Path::

    nano ~/.bashrc

at the bottom of that file (use Page Down key to get there) type::

    export PATH="$PATH:$HOME/pybashutils"


Examples
---------
1. Mounting the "U" network drive at Boston University over SSHFS (slight modifications to the script allow using this anywhere)

one time setup::

    mkdir ~/U

2. mount U drive to your PC, like "mounting a network drive" in Windows, here we assume the BU username is ``jdoe``::

    mU jdoe

and your network drive is available as ~/U

3. Unmounting the "U" drive. When done for the day, suggest unmounting in case to help mitigate security risks::

    uU

Note
~~~~
if you have any files open (like say a spreadsheet on the ~/U drive), ~/U will stay connected until you close that file(s).


Notes:
------
If you get a "sshfs: command not found" error, you need to install sshfs, with a command like::

    sudo apt-get install sshfs

you need "admin" priviledges to install sshfs.
