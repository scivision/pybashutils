#!/usr/bin/env python
import pytest
try:
    import pybashutils.ulimit as ulimit
except ImportError:
    ulimit = None


@pytest.mark.skipif(ulimit is None, reason='Unix only')
def test_ulimit():
    soft, hard = ulimit.raise_nofile(4096)

    assert soft >= 4096
    assert hard >= 4096


if __name__ == '__main__':
    pytest.main()
