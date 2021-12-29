#!/usr/bin/env python3
"""
Terminates particular process/PID if disk free space too low.

E.g. use with crontab to check every 10 minutes or hour, stopping a disk-writing process.

python diskfree_sigterm.py ~ mylogger
"""

from __future__ import annotations
from pathlib import Path
import subprocess
import shutil
import os
import signal
import logging
from argparse import ArgumentParser

SIG = signal.SIGTERM


def diskfree_sigterm(
    disk: str | Path, pid: list, freethres: int, verbose: bool = False
):
    def _stop(pid: int):
        if verbose:
            print("sending", SIG, "to", pid)
        os.kill(pid, SIG)

    disk = Path(disk).expanduser().resolve().anchor

    du = shutil.disk_usage(disk)

    freerat = du.free / du.total
    if freerat < freethres:
        for p in pid:
            if isinstance(p, str):
                try:
                    pstr = subprocess.check_output(
                        ["pgrep", "-f", p], timeout=10, universal_newlines=True
                    )
                except Exception:
                    logging.error(f"did not find PID for {p}")
                for s in pstr.split():
                    _stop(int(s))

            _stop(p)

    if verbose:
        print(f"{disk} free percentage {freerat*100:.1f}")


def main():
    p = ArgumentParser()
    p.add_argument("disk", help="disk path to check")
    p.add_argument(
        "pid", help="process name or PID to terminate if disk space low", nargs="+"
    )
    p.add_argument(
        "-freethres", help="minimum frace free before sigterm", default=0.1, type=float
    )
    p.add_argument("-v", "--verbose", action="store_true")
    P = p.parse_args()

    try:
        pid = list(map(int, P.pid))
    except ValueError:  # name
        pid = P.pid

    diskfree_sigterm(P.disk, pid, P.freethres, P.verbose)


if __name__ == "__main__":
    main()
