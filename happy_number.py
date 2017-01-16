#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_happy(n):
    """TODO: Docstring for is_happy.

    :n: TODO
    :returns: TODO

    """
    s = str(n)
    tick = 30
    while s != '1':
        print s
        if tick <= 0:
            return False
        r =0
        for i in list(s):
            r += int(i)**2
        s = str(r)
        tick -= 1
    return True

print is_happy(19)
