#!/usr/bin/env python
# -*- coding: utf-8 -*-

def longestPalindrome(s):
    """TODO: Docstring for longestPalindrome.

    :s: TODO
    :returns: TODO

    """
    tmpSet = set(s)
    result = 0
    center = 0
    for i in tmpSet:
        num = s.count(i)
        if num => 2:
            if not num % 2:
                result += num 
            else:
                result += num - 1
                center = 1
        else:
            center = 1
    return result + center
