#!/usr/bin/env python
# -*- coding: utf-8 -*-

def selfDividingNumbers(self, left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    result = []
    for i in xrange(left, right+1):
        temp = i
        while temp > 0:
            if temp < 10:
                if i % temp != 0:
                    break
                temp /= 10
            elif temp % 10 == 0:
                break
            elif (i % (temp % 10)) == 0:
                temp /= 10
            else:
                break
        else:
            result.append(i)
    return result
