#!/usr/bin/env python
from pythonutils.windows_linux_detect import Os

for k, v in Os().__dict__.items():
    if v:
        print(k)
