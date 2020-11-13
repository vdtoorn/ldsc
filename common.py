#!/usr/bin/env python

from functools import reduce

MASTHEAD = "*********************************************************************\n"

__version__ = '1.0.7'

def sec_to_str(t):
    """Convert seconds to days:hours:minutes:seconds"""
    [d, h, m, s, n] = reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t, 1), 60, 60, 24])
    f = ''
    if d > 0:
        f += '{D}d:'.format(D=d)
    if h > 0:
        f += '{H}h:'.format(H=h)
    if m > 0:
        f += '{M}m:'.format(M=m)

    f += '{S}s'.format(S=s)
    return f

class Logger(object):
    """
    Lightweight logging.
    TODO: replace with logging module

    """
    def __init__(self, fh):
        self.log_fh = open(fh, 'wt')

    def __del__(self):
        self.log_fh.close()

    def log(self, msg):
        """
        Print to log file and stdout with a single command.

        """
        print(msg, file=self.log_fh)
        print(msg)