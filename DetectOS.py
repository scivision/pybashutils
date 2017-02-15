#!/usr/bin/env python
"""
Provides a Matlab/Octave-like "isX" for fine-grained OS detection
"""
from pythonutils.windows_linux_detect import Os

if __name__ == '__main__':
    for k,v in Os().__dict__.items():
        if v:
            print(k)
