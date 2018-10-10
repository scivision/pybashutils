#!/usr/bin/env python
"""
Demo for Os class, allowing fine-grained Windows Cygwin/WSL OS detection not available in Python standard library
"""
from pybashutils.os_detect import Os


def main():
    print(Os())


if __name__ == '__main__':
    main()
