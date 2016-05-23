#!/usr/bin/env python

from socket import socket

s = socket()
s.bind(('',0))
print(s.getsockname()[1])  #stdout
s.close() #slight race condition
