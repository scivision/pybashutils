#!/usr/bin/env python
import resource as res

def raise_nofile(nofile_atleast=4096,verbose=False):
    """
    sets nofile soft limit to at least 4096, useful for running matlplotlib/seaborn on
    parallel executing plot generators vs. Ubuntu 16.04 default ulimit -n 1024
    """
#%% (0) what is current ulimit -n setting?
    soft,hard = res.getrlimit(res.RLIMIT_NOFILE)
    if verbose: print('current ulimit -n soft,hard: {},{}'.format(soft,hard))
#%% (1) increase limit (soft and even hard) if needed
    if soft<nofile_atleast:
        soft = nofile_atleast

        if hard<soft:
            hard = soft

        print('setting soft & hard ulimit -n {} {}'.format(soft,hard))
        res.setrlimit(res.RLIMIT_NOFILE,(soft,hard))



if __name__ == '__main__':
    raise_nofile(verbose=True)