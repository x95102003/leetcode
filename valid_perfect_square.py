#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_perfect_square(num):
    """TODO: Docstring for is_perfect_square.

    :num: int
    :returns: bool

    """
    mod = 2 
    prev = num
    if num == 1:
        return True
    while True:
        print mod
        t = pow(mod, 2)
        if t > num:
            print prev, mod
            for i in xrange(prev+1, mod):
                print i,num
                if pow(i, 2) == num:
                    return True
            return False
        elif t == num:
            return True
        prev = mod
        mod **= 2 


print is_perfect_square(9)
print is_perfect_square(16)
print is_perfect_square(1)
print is_perfect_square(0)
