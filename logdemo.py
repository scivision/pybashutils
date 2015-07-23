#!/usr/bin/env python3

import logging
logging.basicConfig(format='%(asctime)s %(filename)s/%(funcName)s:%(lineno)d %(message)s', datefmt='%m/%d/%Y %H:%M:%S')


def alwaysfail():
	logging.warning('is when this event was logged.')

if __name__ == '__main__':
	alwaysfail()
