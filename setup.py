#!/usr/bin/env python
install_requires=['colorama','binaryornot']
tests_require=['pytest','nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='pythonutils',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      version='0.6.0',
      description='Cross-platform utilities for computer maintenance',
      long_description=open('README.rst').read(),
      url='https://github.com/scivison/pybashutils',
      classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Environment :: Console',
      'Intended Audience :: Information Technology',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Topic :: Utilities',
      ],
      install_requires=install_requires,
      python_requires='>=3.5',
      tests_require=tests_require,
      extras_require={'tests':tests_require,'io':['pycurl']},
      scripts=['demo_windows_linux_detect.py', 'diskfree_sigterm.py','findvid.py',
      'memfree.py','spellcheck.py','DetectOS.py','find_bad_characters.py','getIP.py',
      'pydeptree.py','tarcp.py','diffdir.py','findtext.py','h5tester.py','whichos.py'],

	  )
