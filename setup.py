#!/usr/bin/env python
req = ['nose','colorama','binaryornot']
# %%
from setuptools import setup

setup(name='pythonutils',
      packages=['pythonutils'],
      author='Michael Hirsch, Ph.D.',
      description='Cross-platform utilities for computer maintenance',
      url='https://github.com/scivison/pybashutils',
      install_requires=req,
      python_requires='>=3.5',
	  )
