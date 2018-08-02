#!/usr/bin/env python
"""requires pycurl which has been a problem on Travis CI (why?)"""
import pytest


def test_getip():
    getip = pytest.importorskip('pybashutils.getIP')

    addr = getip()
    assert len(addr) > 0


if __name__ == '__main__':
    pytest.main(['-x', __file__])
