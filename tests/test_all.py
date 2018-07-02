#!/usr/bin/env python
import pytest
from pybashutils.getfreeport import freeport
import pybashutils.ulimit as ulimit
from pybashutils.windows_linux_detect import Os


def test_getfreeport():

    port = freeport()
    assert isinstance(port, int)


def test_ulimit():
    soft, hard = ulimit.raise_nofile(4096)

    assert soft >= 4096
    assert hard >= 4096


def test_os():
    a = []
    for k, v in Os().__dict__.items():
        if v:
            a.append(k)
    assert len(k) > 1


if __name__ == '__main__':
    pytest.main()
