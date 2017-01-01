#!/usr/bin/env python
# -*- coding: utf-8 -*-

def find_the_difference(s, t):
    r = 0 
    for i in s+t:
        r ^= ord(i)
    return chr(r)
print find_the_difference(s = 'abcd', t = 'abcde')
