#!/usr/bin/env python
install_requires=['colorama','binaryornot']
tests_require=['pytest','nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='pythonutils',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      version='0.5.1',
      description='Cross-platform utilities for computer maintenance',
      long_description=open('README.rst').read(),
      url='https://github.com/scivison/pybashutils',
      install_requires=install_requires,
      python_requires='>=3.5',
      tests_require=tests_require,
      extras_require={'tests':tests_require},
	  )
