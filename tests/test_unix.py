#!/usr/bin/env python
import pytest


def test_ulimit():

    ulimit = pytest.importorskip('pybashutils.ulimit')

    soft, hard = ulimit.raise_nofile(4096)

    assert soft >= 4096
    assert hard >= 4096


if __name__ == '__main__':
    pytest.main(['-x', __file__])
