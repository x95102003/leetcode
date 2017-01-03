#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isAnagram(s, t):
    """TODO: Docstring for isAnagram.

    :s: TODO
    :t: TODO
    :returns: TODO

    """
    return ''.join(sorted(s)) == ''.join(sorted(t)) 

print isAnagram('', '')
