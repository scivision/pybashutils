[![Build Status](https://travis-ci.org/scienceopen/pybashutils.svg)](https://travis-ci.org/scienceopen/pybashutils)
[![Coverage Status](https://coveralls.io/repos/scienceopen/pybashutils/badge.svg)](https://coveralls.io/r/scienceopen/pybashutils)
[![Code Climate](https://codeclimate.com/github/scienceopen/pybashutils/badges/gpa.svg)](https://codeclimate.com/github/scienceopen/pybashutils)

bash-utils
==========

```cupd```: update conda packages (well, the ones I use)

```checkIP```: Sends you an email automatically if your IP address changes

```getIP```: gets your public IP address (not the internal NAT address)

```findtext```: find text inside files matching pattern.

mx: mount network share example using SSHFS

Collection of Bash scripts I've made that may be generally useful

Installation:
-------------
(1) download the code
```
cd ~
git clone --depth 1 https://github.com/scienceopen/pybashutils.git
```
(2) add the scripts to your Path:
```
nano ~/.bashrc
```
at the bottom of that file (use Page Down key to get there) type:
```
export PATH="$PATH:$HOME/pybashutils"
```

Examples:
---------
(1) Mounting the "U" network drive at Boston University over SSHFS (slight modifications to the script allow using this anywhere)
####one time setup
```
mkdir ~/U
```
#### mount U drive to your PC, like "mounting a network drive" in Windows, here we assume the BU username is ``` jdoe ```

```
mU jdoe
```
and your network drive is available as ~/U

(2) Unmounting the "U" drive. When done for the day, suggest unmounting in case to help mitigate security risks.
```
uU
```
Note: if you have any files open (like say a spreadsheet on the ~/U drive), ~/U will stay connected until you close that file(s).
