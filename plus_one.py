#!/usr/bin/env python
# -*- coding: utf-8 -*-

def plus_one(digits):
    """

    :digits: List[int]
    :returns: List[int]

    """
    flip = 0
    digits[-1] += 1
    dlen = len(digits)
    for i in xrange(dlen-1, -1, -1):
        digits[i] += flip
        if digits[i] >= 10:
            digits[i] = 0
            flip = 1
        else:
            flip = 0
    if flip:
        digits.insert(0, flip)
    return digits
