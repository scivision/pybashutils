#!/usr/bin/env python3
from urllib.request import urlopen

print(urlopen("https://ident.me").read().decode("ascii"))
