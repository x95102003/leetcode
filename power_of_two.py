#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_power_of_two(n):
    """TODO: Docstring for is_power_of_two.

    :n: TODO
    :returns: TODO

    """
    b = bin(n)
    return bin(n).count('1') == 1 if n > 0 else False

for i in xrange(9999999):
    if is_power_of_two(i):
        print i
for i in xrange(20):
    print i**2
