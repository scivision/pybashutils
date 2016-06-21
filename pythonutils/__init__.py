#!/usr/bin/env python
from six import PY2
if PY2:
    from pathlib2 import Path
else:
    from pathlib import Path