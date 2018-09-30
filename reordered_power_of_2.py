#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reorderedPowerOf2(N):
    """
    :type N: int
    :rtype: bool
    """
    from collections import Counter
    result = []
    for i in xrange(30):
        result.append(Counter(str(2**i)))
    if Counter(str(N)) in result:
        return True
    return False 

if __name__ == '__main__':
    print(reorderedPowerOf2(46))
