#!/usr/bin/env python
import os
import pybashutils.ulimit as ulimit
import pytest


@pytest.mark.skipif(os.name == 'nt', reason='Unix only')
def test_ulimit():
    soft, hard = ulimit.raise_nofile(4096)

    assert soft >= 4096
    assert hard >= 4096


if __name__ == '__main__':
    pytest.main()
