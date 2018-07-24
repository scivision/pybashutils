#!/usr/bin/env python
"""requires pycurl which has been a problem on Travis CI (why?)"""
import pytest
try:
    import pycurl
except ImportError:
    pycurl = None


@pytest.mark.skipif(pycurl is None, reason="PyCurl is optional")
def test_getip():
    from pybashutils.getIP import getip
    addr = getip()
    assert len(addr) > 0


if __name__ == '__main__':
    pytest.main()
