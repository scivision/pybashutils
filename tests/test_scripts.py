#!/usr/bin/env python
import subprocess
import pytest


def test_findtext():
    ret = subprocess.check_output(['findtext', 'import'], universal_newlines=True)

    assert isinstance(ret, str)
    assert len(ret) > 0


if __name__ == '__main__':
    pytest.main(['-x', __file__])
