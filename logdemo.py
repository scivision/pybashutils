#!/usr/bin/env python3
"""
If you have a project with multiple .py files, you can log them all to this logger here by in each file doing
import logging

that's it!
"""

import logging
logging.basicConfig(format='%(asctime)s %(filename)s/%(funcName)s:%(lineno)d %(message)s', datefmt='%m/%d/%Y %H:%M:%S')


def alwaysfail():
	logging.warning('is when this event was logged.')

if __name__ == '__main__':
	alwaysfail()
