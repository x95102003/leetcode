#!/usr/bin/env python
# -*- coding: utf-8 -*-

def titleToNumber(s):
    """TODO: Docstring for titleToNumber.

    :s: TODO
    :returns: TODO

    """
    num = 0
    for idx, c in enumerate(s[::-1]):
        dif = ord(c) - 64
        num += dif * (26 ** idx)
    return num

print titleToNumber('AB')
