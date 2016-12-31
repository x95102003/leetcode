#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum_of_twn_nums(a, b):
    """TODO: Docstring for sum_of_twn_nums.

    :a: TODO
    :b, TODO
    :returns: TODO

    """
    carry = 0
    result = []
    mlen = max(len(bin(a)), len(bin(b)))
    for i, j in zip(bin(a)[2:].zfill(mlen)[::-1], bin(b)[2:].zfill(mlen)[::-1]):
        print i, j, carry,i^j^carry
        i = int(i)
        j = int(j)
        result.insert(0, str(i ^ j ^ carry))
        if i & j or i & carry or j & carry:
            carry = 1
        else:
            carry = 0
    result.insert(0, str(carry))
    
    return int(''.join(result), 2)
print sum_of_twn_nums(-1, 1)

