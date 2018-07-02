#!/usr/bin/env python
"""
platform-independent free memory to stdout in bytes
"""
import psutil


def main():
    print(psutil.virtual_memory().available)


if __name__ == '__main__':
    main()
