#!/usr/bin/env python3
"""
If you have a project with multiple .py files, you can log them all to this logger here by in each file doing
import logging

that's it!

By default, logging will log to stderr (on your console)


Ref: http://stackoverflow.com/questions/6290739/python-logging-use-milliseconds-in-time-format
"""

import logging
logging.basicConfig(format='%(asctime)s.%(msecs)03d %(filename)s/%(funcName)s:%(lineno)d %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def alwaysfail():
    logging.warning('is when this event was logged.')


if __name__ == '__main__':
    alwaysfail()
