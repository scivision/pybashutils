#!/usr/bin/env python
req = ['nose','colorama','binaryornot']
# %%
from setuptools import setup,find_packages

setup(name='pythonutils',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      description='Cross-platform utilities for computer maintenance',
      url='https://github.com/scivison/pybashutils',
      install_requires=req,
      python_requires='>=3.5',
	  )
