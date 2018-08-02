#!/usr/bin/env python
import subprocess
import pytest
from pathlib import Path

R = Path(__file__).parent


def test_findtext():
    ret = subprocess.check_output(['findtext', 'import'], universal_newlines=True, cwd=R)

    assert isinstance(ret, str)
    assert len(ret) > 0


if __name__ == '__main__':
    pytest.main(['-x', __file__])
