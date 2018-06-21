#!/usr/bin/env python
from setuptools import setup, find_packages
from pathlib import Path

install_requires = ['colorama', 'binaryornot']
tests_require = ['pytest', 'coveralls', 'flake8', 'mypy']

scripts = [s.name for s in Path(__file__).parent.glob('*.{sh,py}') if not s.name == 'setup.py']


setup(name='pybashutils',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      version='0.6.1',
      description='Cross-platform utilities for computer maintenance',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      url='https://github.com/scivison/pybashutils',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Information Technology',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Utilities',
      ],
      install_requires=install_requires,
      python_requires='>=3.6',
      tests_require=tests_require,
      extras_require={'tests': tests_require, 'io': ['pycurl']},
      scripts=scripts,

      )
