#!/usr/bin/env python
# -*- coding: utf-8 -*-

def addStrings(num1, num2):
    """TODO: Docstring for addStrings.

    :num1: TODO
    :num2: TODO
    :returns: TODO

    """ 
    mx_len = max(len(num1), len(num2))
    num1 = num1.zfill(mx_len)
    num2 = num2.zfill(mx_len)
    flip = 0
    result = ''
    print num1, num2
    for n1, n2 in zip(num1[::-1], num2[::-1]):
        tmp = int(n1) + int(n2) + flip
        result += str(tmp % 10)
        flip = tmp / 10
    if flip != 0:
        result += str(flip)
    return result[::-1]
