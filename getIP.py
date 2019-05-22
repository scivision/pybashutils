#!/usr/bin/env python
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen  # type: ignore

print(urlopen('https://ident.me').read().decode('ascii'))
