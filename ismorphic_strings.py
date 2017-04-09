#!/usr/bin/env python
# -*- coding: utf-8 -*-
def isIsomorphic(self, s, t):
    """
    Use the index to check whether the element exist.
    :type s: str
    :type t: str
    :rtype: bool
    """
    return map(s.find, s) == map(t.find, t)
