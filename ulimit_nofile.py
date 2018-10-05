#!/usr/bin/env python
from argparse import ArgumentParser
import pybashutils.ulimit as ulimit


def main():
    p = ArgumentParser()
    p.add_argument('-n', '--nofile', help='max number of open files',
                   type=int, default=4096)
    P = p.parse_args()

    soft, hard = ulimit.raise_nofile(P.nofile)
    print(f'ulimit -n soft, hard:  {soft}, {hard}')


if __name__ == '__main__':
    main()
