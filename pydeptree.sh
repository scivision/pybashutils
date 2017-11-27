#!/bin/bash

set -e

[[ ! -z $1 ]] && cd $1

virtualenv testdep     # it's OK if it already exists
. testdep/bin/activate

pip install pipdeptree[graphviz]

pip install -e .[tests]

python ~/code/pybashutils/pydeptree.py --graph-output svg > dep.svg

python setup.py nosetests --exe

. deactivate

eog dep.svg&  # whatever your favorite image viewing program is
