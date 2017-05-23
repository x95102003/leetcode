#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    else:
        return not (x - self.reverseInt(x))
        
def reverseInt(self, a):
    """
        reverse int number
    """
    c = 0
    while a != 0:
        d, a = a %10, a/10
        c = c * 10 + d
    return c
