#!/usr/bin/env python
"""
gets interface IPv4 and IPv6 public addresses using libCURL
This uses the "reflector" method, which I feel is more reliable for finding public-facing IP addresses,
WITH THE CAVEAT that man-in-the-middle, etc. attacks can defeat the reflector method.
"""
from ipaddress import ip_address
import pycurl
from io import BytesIO

urls = ['https://ident.me','http://wtfismyip.com/text', # ipv6 and ipv4
        'https://ipecho.net/plain','https://api.ipify.org'] # ipv4 only
length=45 #http://stackoverflow.com/questions/166132/maximum-length-of-the-textual-representation-of-an-ipv6-address

def getip():
    for url in urls:
        addr = []
        for ipv in (pycurl.IPRESOLVE_V4,pycurl.IPRESOLVE_V6):
            buffer = BytesIO() # must clear like this
            C = pycurl.Curl()
            C.setopt(C.URL, url)
            C.setopt(pycurl.IPRESOLVE, ipv)
            C.setopt(C.WRITEDATA, buffer)
            try:
                C.perform()
                result = buffer.getvalue()
                try: #validate response
                    addr.append(ip_address(result.decode('utf8')))
                except ValueError:
                    pass
            except pycurl.error:
                pass
            finally:
                C.close()

        if len(addr)>1:
            break

    return addr

if __name__ == '__main__':
    addr = getip()
    print(addr)

