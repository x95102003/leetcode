#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_ugly(num):
    """TODO: Docstring for is_ugly.

    :num: TODO
    :returns: TODO

    """
    if num == 1:
        return True
    elif num == 0:
        return False
    while num != 1:
        if num % 2 == 0:
            num /= 2
            continue
        elif num % 3 == 0:
            num /= 3
            continue
        elif num % 5 == 0:
            num /= 5
            continue
        else:
            return  False
    return True

print is_ugly(35)
print is_ugly(4)
print is_ugly(7)
print is_ugly(14)
print is_ugly(6)
print is_ugly(8)
