#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_power_of_four(num):
    """TODO: Docstring for is_power_of_four.

    :num: TODO
    :returns: TODO

    """
    bnum = bin(num)[2:]
    if bnum[0] == '1':
        remain = bnum[1:]
        zero = remain.count('0')
        if len(remain) == zero and not zero % 2:
            return True
    return False

print is_power_of_four(4)
print is_power_of_four(0)
print is_power_of_four(1)
print is_power_of_four(16)
print is_power_of_four(13)

