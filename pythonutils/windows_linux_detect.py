#!/usr/bin/env python
"""
Provides a Matlab/Octave-like "isX" for fine-grained OS detection
"""

from platform import system

class Os:
    """
    returns class with properties:
    .iscygwin   Cygwin detected
    .iswsl      Windows Subsystem for Linux (WSL) detected
    .ismac      Mac OS detected
    .islinux    Linux detected
    .isbsd      BSD detected
    """

    def __init__(self):
        syst = system().lower()

        #initialize
        self.iscygwin  = False
        self.iswsl     = False
        self.ismac     = False
        self.islunix    = False
        self.iswindows = False

        if 'cygwin' in syst:
            self.iscygwin=True
        elif 'darwin' in syst:
            self.ismac = True
        elif 'linux' in syst:
            self.islinux = True
        elif 'windows' in syst:
            self.iswindows = True
        elif 'bsd' in syst:
            self.isbsd     = True

        # detect WSL https://github.com/Microsoft/BashOnWindows/issues/423
        if self.islinux:
            with open('/proc/version','r') as f:
                vers = f.read()
            if 'microsoft' in vers.lower():
                self.iswsl=True

if __name__ == '__main__':
    for k,v in Os().__dict__.items():
        if v:
            print(k)
