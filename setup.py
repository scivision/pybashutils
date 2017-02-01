#!/usr/bin/env python
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='pythonutils',
	  install_requires=required,
      packages=['pythonutils'],
	  )
