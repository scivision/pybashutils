#!/usr/bin/env python
install_requires=['colorama','binaryornot']
tests_require=['nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='pythonutils',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      version='0.5.0',
      description='Cross-platform utilities for computer maintenance',
      url='https://github.com/scivison/pybashutils',
      install_requires=install_requires,
      python_requires='>=3.5',
      tests_require=tests_require,
      extras_require={'tests':tests_require},
	  )
