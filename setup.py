#!/usr/bin/env python
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='pythonutils',
	  description='Python Utilities generally useful',
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/pybashutils',
	  install_requires=required,
      dependency_links = [],
      packages=['pythonutils'],
	  )
