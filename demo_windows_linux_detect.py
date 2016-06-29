#!/usr/bin/env python
"""
Demo for Os class, allowing fine-grained Windows Cygwin/WSL OS detection not available in Python standard library
"""
from pythonutils.windows_linux_detect import Os

winos = Os()

print('Windows {}'.format(winos.iswindows))
print('Cygwin? {}'.format(winos.iscygwin))
print('WSL? {}'.format(winos.iswsl))
