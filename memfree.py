#!/usr/bin/env python3
"""
platform-independent free memory to stdout in bytes
"""

import psutil

print(psutil.virtual_memory().available)
