#!/usr/bin/env python
"""
Demo for Os class, allowing fine-grained Windows Cygwin/WSL OS detection not available in Python standard library
"""
from pybashutils.windows_linux_detect import Os

winos = Os()

print('Windows', winos.windows)
print('Cygwin', winos.cygwin)
print('WSL', winos.wsl)
print('Linux', winos.linux)
print('BSD', winos.bsd)
print('Mac', winos.mac)
