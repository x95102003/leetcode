#!/usr/bin/env python
# -*- coding: utf-8 -*-

def strStr(self, haystack, needle):
    """
    Implement the indexOf function, each length must include substr size.
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    j, pos = 0, -1
    check = False
    nlen = len(needle)
    hlen = len(haystack)
    if nlen == 0:
        return 0
    for i in xrange(hlen - nlen + 1):
        for j, v in enumerate(needle):
            if haystack[i+j] == v:
                check = True
                continue
            else:
                check = False
                break
        if check:
            return i
    return -1
