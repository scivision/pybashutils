#!/usr/bin/env python
"""
gets interface IPv4 and IPv6 public addresses using libCURL
This uses the "reflector" method, which I feel is more reliable for finding public-facing IP addresses,
WITH THE CAVEAT that man-in-the-middle, etc. attacks can defeat the reflector method.

PyCurl does not have a context manager.
"""
import logging
from ipaddress import ip_address
import pycurl
from io import BytesIO
from typing import List

URL = 'https://ident.me' # ipv6 and ipv4
#URL = 'https://api.ipify.org' # ipv4 only
length=45 #http://stackoverflow.com/questions/166132/maximum-length-of-the-textual-representation-of-an-ipv6-address

def getip(iface:str=None) -> List[ip_address]:
    return [_public_addr(v,iface) for v in (pycurl.IPRESOLVE_V4,pycurl.IPRESOLVE_V6)]

def _public_addr(v, iface:str=None) -> ip_address:
    B = BytesIO()
    C = pycurl.Curl()
# %% set options    
    C.setopt(pycurl.TIMEOUT, 3) # 1 second is too short for slow connections
    if iface:
        C.setopt(pycurl.INTERFACE, iface)
    C.setopt(C.URL, URL)
    C.setopt(pycurl.IPRESOLVE, v)
    C.setopt(C.WRITEDATA, B)
# %% get public IP address
    try:
        C.perform()
        result = B.getvalue()
        try: #validate response
            return ip_address(result.decode('utf8'))
        except ValueError as e:
            logging.error(f'could not determine IP address:  {e}')
            return
    except pycurl.error as e:
        #logging.error(f'could not determine IP address:  {e}')
        return
    finally:   
        C.close()

 

if __name__ == '__main__':
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('iface',help='network interface to use',nargs='?')
    p = p.parse_args()

    addr = getip(p.iface)
    print(addr)

