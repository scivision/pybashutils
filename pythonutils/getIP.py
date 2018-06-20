import logging
import ipaddress
import pycurl
from io import BytesIO
from typing import List, Union

length = 45  # http://stackoverflow.com/questions/166132/maximum-length-of-the-textual-representation-of-an-ipv6-address

URL = 'https://ident.me'


def getip(url: str=None, iface: str=None) -> List[Union[ipaddress.IPv4Address, ipaddress.IPv6Address]]:
    if url is None:
        url = URL

    addrs = []
    for v in (pycurl.IPRESOLVE_V4, pycurl.IPRESOLVE_V6):
        addr = _public_addr(v, url, iface)
        if addr is not None:
            addrs.append(addr)

    return addrs


def _public_addr(v, url: str, iface: str=None) -> Union[None, ipaddress.IPv4Address, ipaddress.IPv6Address]:
    B = BytesIO()
    C = pycurl.Curl()
# %% set options
    C.setopt(pycurl.TIMEOUT, 3)  # 1 second is too short for slow connections
    if iface:
        C.setopt(pycurl.INTERFACE, iface)
    C.setopt(C.URL, url)
    C.setopt(pycurl.IPRESOLVE, v)
    C.setopt(C.WRITEDATA, B)
# %% get public IP address
    try:
        C.perform()
        result = B.getvalue()
        try:  # validate response
            return ipaddress.ip_address(result.decode('utf8'))
        except ValueError as e:
            logging.error(f'could not determine IP address:  {e}')
            return None
    except pycurl.error as e:
        # logging.error(f'could not determine IP address:  {e}')
        return None
    finally:
        C.close()
