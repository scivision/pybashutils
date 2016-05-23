#!/usr/bin/env python
from setuptools import setup


with open('README.rst','r') as f:
	long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='pythonutils',
      version='0.1',
	  description='Python Utilities generally useful',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/pybashutils',
	  install_requires=required,
      dependency_links = [],
      packages=['pythonutils'],
	  )
