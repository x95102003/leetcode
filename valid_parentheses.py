#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_valid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    hash_set = {'(':')', '[':']', '{':'}'}
    for v in s:
        if v in hash_set:
            stack.append(v)
        else:
            if len(stack) > 0:
                if hash_set[stack.pop()] == v:
                    continue
                else:
                    return False
            return False
    if len(stack) != 0:
        return False
    return True
