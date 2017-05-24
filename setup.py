#!/usr/bin/env python

req = ['nose','colorama',]
pipreq=['binaryornot']
import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception as e:    
    pip.main(['install'] + req)
pip.main(['install'] + pipreq)
# %%
from setuptools import setup

setup(name='pythonutils',
      packages=['pythonutils'],
      author='Michael Hirsch, Ph.D.',
      description='Cross-platform utilities for computer maintenance',
      url='https://github.com/scivison/pybashutils',
	  )
