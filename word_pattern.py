#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wordPattern(self, pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    dic = {}
    slist = str.split(' ')
    if len(pattern) != len(slist):
        return False
    for p, v in zip(pattern, slist):
        if p not in dic:
            if v in dic.values():
                return False
            else:
                dic.update({p:v})
        else:
            if dic[p] != v:
                print dic[p], v
                return False
    return True
