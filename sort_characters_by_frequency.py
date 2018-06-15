#!/usr/bin/env python
# -*- coding: utf-8 -*-

def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    result = {}
    ans = ''
    for c in s:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1 
    for e in (sorted(result.items(), key=lambda t:t[1],reverse=True)):
        ans += e[0] * e[1]
    return ans
    

if __name__ == '__main__':
    frequencySort('ccbbasdcvbb')
