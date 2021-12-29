#!/usr/bin/env python3

"""
gets interface IPv4 and IPv6 public addresses using libCURL
This uses the "reflector" method, which I feel is more reliable for finding public-facing IP addresses,
WITH THE CAVEAT that man-in-the-middle, etc. attacks can defeat the reflector method.

PyCurl does not have a context manager.

https://ident.me  ipv6 and ipv4
https://api.ipify.org # ipv4 only
"""

from __future__ import annotations
from argparse import ArgumentParser
import ipaddress
import pycurl
from io import BytesIO


length = 45  # http://stackoverflow.com/questions/166132/maximum-length-of-the-textual-representation-of-an-ipv6-address

URL = "https://ident.me"


def main():
    p = ArgumentParser()
    p.add_argument("iface", help="network interface to use", nargs="?")
    p.add_argument("--url", help="plain text server", default="https://ident.me")
    P = p.parse_args()

    addr = getip(P.url, P.iface)
    for a in addr:
        print(a)


def getip(
    url: str = None, iface: str = None
) -> list[ipaddress.IPv4Address | ipaddress.IPv6Address]:
    if url is None:
        url = URL

    addrs = []
    for v in (pycurl.IPRESOLVE_V4, pycurl.IPRESOLVE_V6):
        addr = _public_addr(v, url, iface)
        if addr is not None:
            addrs.append(addr)

    return addrs


def _public_addr(
    v, url: str, iface: str = None
) -> ipaddress.IPv4Address | ipaddress.IPv6Address:
    B = BytesIO()
    C = pycurl.Curl()
    addr = None
    # %% set options
    C.setopt(pycurl.TIMEOUT, 3)  # 1 second is too short for slow connections
    if iface:
        C.setopt(pycurl.INTERFACE, iface)
    C.setopt(C.URL, url)  # type: ignore
    C.setopt(pycurl.IPRESOLVE, v)
    C.setopt(C.WRITEDATA, B)  # type: ignore
    # %% get public IP address
    ret = None
    try:
        C.perform()
        ret = B.getvalue()
        C.close()
    except pycurl.error:
        pass
    # %% validate response
    if ret:
        addr = ipaddress.ip_address(ret.decode("utf8"))

    return addr


if __name__ == "__main__":
    main()
