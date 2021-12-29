#!/usr/bin/env python
import pytest
from pybashutils.getfreeport import freeport
from pybashutils.os_detect import Os


def test_getfreeport():

    port = freeport()
    assert isinstance(port, int)


def test_os():
    os = str(Os())

    assert isinstance(os, str) and len(os) >= 3


if __name__ == "__main__":
    pytest.main(["-x", __file__])
