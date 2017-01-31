#!/usr/bin/env python
"""
Provides a Matlab/Octave-like "isX" for fine-grained OS detection

This is a standalone script you can copy out of this repo.
"""

from platform import system

class Os:
    """
    returns class with properties:
    .cygwin   Cygwin detected
    .wsl      Windows Subsystem for Linux (WSL) detected
    .mac      Mac OS detected
    .linux    Linux detected
    .bsd      BSD detected
    """

    def __init__(self):
        syst = system().lower()

        #initialize
        self.cygwin  = False
        self.wsl     = False
        self.mac     = False
        self.linux   = False
        self.windows = False
        self.bsd     = False

        if 'cygwin' in syst:
            self.cygwin = True
        elif 'darwin' in syst:
            self.mac    = True
        elif 'linux' in syst:
            self.linux  = True
        elif 'windows' in syst:
            self.windows= True
        elif 'bsd' in syst:
            self.bsd    = True

        # detect WSL https://github.com/Microsoft/BashOnWindows/issues/423
        if self.linux:
            with open('/proc/version','r') as f:
                vers = f.read()
            if 'microsoft' in vers.lower():
                self.wsl = True

if __name__ == '__main__':
    for k,v in Os().__dict__.items():
        if v:
            print(k)
