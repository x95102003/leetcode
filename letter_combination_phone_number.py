#!/usr/bin/env python
# -*- coding: utf-8 -*-

def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    def inner(str_a,str_b):
            return [a + b for a in str_a for b in str_b]
    mapping = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv','9':'wxyz'}
    if '0' in digits or '1' in digits or not digits:
        return []
    dlen = len(digits)
    result = list(mapping[digits[0]])
    if dlen == 1:
        return result

    for idx in xrange(1, dlen):
        result = inner(result, mapping[digits[idx]])
    return result
