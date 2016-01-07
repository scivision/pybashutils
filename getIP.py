#!/usr/bin/env python3
from six.moves.urllib.request import urlopen

urls = ['https://wtfismyip.com/text','https://api.ipify.org','http://ident.me','http://ipecho.net/plain']
len=45 #http://stackoverflow.com/questions/166132/maximum-length-of-the-textual-representation-of-an-ipv6-address

for url in urls:
    try:
        print(urlopen(url).read(len).split()[0].decode('ascii'))
        exit()
    except Exception:
        pass
