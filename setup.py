#!/usr/bin/env python
import os,sys,subprocess
from setuptools import setup

exepath = os.path.dirname(sys.executable)
try:
    subprocess.run([os.path.join(exepath,'conda'),'install','--yes','--file','requirements.txt'])
except Exception as e:
    print('tried conda in {}, but you will need to install packages in requirements.txt  {}'.format(exepath,e))

with open('README.rst','r') as f:
	long_description = f.read()

setup(name='pythonutils',
      version='0.1',
	  description='Python Utilities generally useful',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/pybashutils',
	  install_requires=[],
      dependency_links = [],
      packages=['pythonutils'],
	  )
