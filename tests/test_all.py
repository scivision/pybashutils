#!/usr/bin/env python
import pytest
from pybashutils.getfreeport import freeport
from pybashutils.windows_linux_detect import Os


def test_getfreeport():

    port = freeport()
    assert isinstance(port, int)


def test_os():
    a = []
    for k, v in Os().__dict__.items():
        if v:
            a.append(k)
    assert len(k) > 1


if __name__ == '__main__':
    pytest.main()
