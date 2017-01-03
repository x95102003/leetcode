#!/usr/bin/env python
# -*- coding: utf-8 -*-

def firstUniqChar(s):
    """TODO: Docstring for firstUniqChar.

    :s: TODO
    :returns: TODO

    """
    s_len = len(s)
    tmp = []
    if s_len == 0:
        return -1
    for i, v in enumerate(s):
        if v not in s[i+1:] and v not in tmp:
                return i
        else:
            tmp.append(v)
    return -1
