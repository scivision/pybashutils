#!/bin/bash

set -e

[[ ! -z $1 ]] && cd $1

virtualenv testdep     # it's OK if it already exists

. testdep/bin/activate

pip install pipdeptree[graphviz]

pip install -e .[tests]   # extras_require={'tests':['nose','coveralls']}

python ~/code/pybashutils/pydeptree.py --graph-output svg > dep.svg

. deactivate

eog dep.svg &  # whatever your favorite image viewing program is
