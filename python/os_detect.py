from platform import system, uname


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

        match syst:
            case "cygwin":
                self.cygwin = True
                self.os = "cygwin"
            case "darwin":
                self.mac = True
                self.os = "mac"
            case "linux":
                self.linux = True
                self.os = "linux"
                if "Microsoft" in uname().release:
                    self.wsl = True
                    self.linux = False
                    self.os = "wsl"
            case "windows":
                self.windows = True
                self.os = "windows"
            case "bsd":
                self.bsd = True
                self.os = "bsd"
            case _:
                self.os = "unknown"

    def __str__(self):
        return self.os


if __name__ == "__main__":
    print(Os())
