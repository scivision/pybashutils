
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

        # initialize
        self.cygwin = False
        self.wsl = False
        self.mac = False
        self.linux = False
        self.windows = False
        self.bsd = False

        if 'cygwin' in syst:
            self.cygwin = True
        elif 'darwin' in syst:
            self.mac = True
        elif 'linux' in syst:
            self.linux = True
            # detect WSL https://github.com/Microsoft/BashOnWindows/issues/423
            with open('/proc/version', 'r') as f:
                if 'microsoft' in f.read().lower():
                    self.wsl = True
                    self.linux = False
        elif 'windows' in syst:
            self.windows = True
        elif 'bsd' in syst:
            self.bsd = True
