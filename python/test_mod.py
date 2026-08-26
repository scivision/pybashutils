from getfreeport import freeport
from os_detect import Os


def test_getfreeport():

    port = freeport()
    assert isinstance(port, int)


def test_os():
    os = str(Os())

    assert isinstance(os, str) and len(os) >= 3
