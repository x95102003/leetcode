#!/usr/bin/env python
# -*- coding: utf-8 -*-

def checkPerfectNumber(self, num):
    """
    find the divisors and its quotient add in result and compare finally.
    :type num: int
    :rtype: bool
    """
    if num < 5:
        return False
    import math
    result = 1
    for i in xrange(2, int(math.sqrt(num))+1):
        if num % i == 0:
            result += i + num / i
    print result
    return result == num
