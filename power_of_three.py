#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_power_of_three(n):
    """TODO: Docstring for is_power_of_three.

    :n: TODO
    :returns: TODO

    """
    s = str(n)
    n_len = len(s)
    tl = [1, 3, 9, 27, 81, 243]
    if n in tl:
        return True
    if s[-1] == '1':
        return n == 3 ** (n_len * 2)
    elif s[-1] == '3':
        return n == 3 ** (n_len * 2 -1)
    elif s[-1] == '9':
        return n == 3 ** (n_len * 2)
    elif s[-1] == '7':
        return n == 3 ** (n_len * 2 -1)
    return False

for i in xrange(999999999):
    if is_power_of_three(i):
        print i

for i in xrange(20):
    print 3**i

