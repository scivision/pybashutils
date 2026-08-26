#!/usr/bin/env python3
"""
checks if you can create a file and symlink to the file

if you get error on Windows:

  OSError: symbolic link privilege not held

see:

https://www.scivision.dev/windows-symbolic-link-permission-enable/
"""

from pathlib import Path
import argparse

p = argparse.ArgumentParser()
p.add_argument("source", help="file to create and link to")
p.add_argument("target", help="where to create the soft / symbolic link")
P = p.parse_args()

source = Path(P.source).expanduser()
target = Path(P.target).expanduser()

if not source.exists():
    source.touch()

print("attempting to symlink", source, target)

target.symlink_to(source, source.is_dir())

assert target.is_symlink(), f"{target} was not linked to {source}"
