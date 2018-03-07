#!/usr/bin/env python
def test_getip(): #requires pycurl which has been a problem on Travis CI (why?)
    from pythonutils.getIP import getip
    addr = getip()
    assert len(addr)>0

def test_getfreeport():
    from pythonutils.getfreeport import freeport

    port = freeport()
    assert isinstance(port,int)

def test_ulimit():
    from pythonutils.ulimit_nofile import raise_nofile

    soft,hard = raise_nofile(4096)

    assert soft>=4096
    assert hard>=4096

def test_os():
    from pythonutils.windows_linux_detect.py import Os
    a = []
    for k,v in Os().__dict__.items():
        if v:
            a.append(k)
    assert len(k) > 1

if __name__ == '__main__':

#	test_getip()
	test_getfreeport()
	test_ulimit()
