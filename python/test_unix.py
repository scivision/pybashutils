import pytest


def test_ulimit():

    soft, hard = ulimit.raise_nofile(4096)

    assert soft >= 4096
    assert hard >= 4096
