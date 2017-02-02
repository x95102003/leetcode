#!/usr/bin/env python
# -*- coding: utf-8 -*-

def arrange_coins(n):
    """TODO: Docstring for arrange_coins.

    :n: int
    :returns: row of coins

    """
    for i in xrange(n/2+2):
        coins = i * (i + 1) / 2
        if coins == n:
           return i
        elif coins > n:
            return i-1
    return 0
