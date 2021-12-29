#!/usr/bin/env python3
"""
Demo for Os class, allowing fine-grained Windows Cygwin/WSL OS detection not available in Python standard library
"""

from pybashutils.os_detect import Os

print(Os())
