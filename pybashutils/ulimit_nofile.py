#!/usr/bin/env python
import resource as res


def raise_nofile(nofile_atleast=4096):
    """
    sets nofile soft limit to at least 4096, useful for running matlplotlib/seaborn on
    parallel executing plot generators vs. Ubuntu 16.04 default ulimit -n 1024 or OS X El Captian 256
    temporary setting extinguishing with Python session.
    """
# %% (0) what is current ulimit -n setting?
    soft, ohard = res.getrlimit(res.RLIMIT_NOFILE)
    hard = ohard
# %% (1) increase limit (soft and even hard) if needed
    if soft < nofile_atleast:
        soft = nofile_atleast

        if hard < soft:
            hard = soft

        print('setting soft & hard ulimit -n {} {}'.format(soft, hard))
        try:
            res.setrlimit(res.RLIMIT_NOFILE, (soft, hard))
        except (ValueError, res.error):
            try:
                hard = soft
                print(
                    'trouble with max limit, retrying with soft,hard {},{}'.format(soft, hard))
                res.setrlimit(res.RLIMIT_NOFILE, (soft, hard))
            except Exception:
                print('failed to set ulimit, giving up')
                soft, hard = res.getrlimit(res.RLIMIT_NOFILE)

    return soft, hard


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('-n', '--nofile',
                   help='max number of open files', type=int, default=4096)
    P = p.parse_args()

    soft, hard = raise_nofile(P.nofile)
    print(f'ulimit -n soft,hard: {soft},{hard}')
