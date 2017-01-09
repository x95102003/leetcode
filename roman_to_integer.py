#!/usr/bin/env python
# -*- coding: utf-8 -*-

def romanToInt(s):
    """TODO: Docstring for romanToInt.

    :s: TODO
    :returns: TODO

    """
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s_len = len(s)
    ans = 0
    midx = s_len-1
    mx = roman[s[midx]]
    for i in xrange(s_len-1):
        value = roman[s[i]]
        next_v = roman[s[i+1]]
        if value >= mx:
            midx = i
            mx = value
        if value < next_v:
            ans -= value
        else:
            ans += value
    last = roman[s[s_len-1]]
    if last > mx:
        return last - ans
    else:
        return ans + last
print romanToInt("DCXXI")
print romanToInt("MDCCCLXXXIV")
