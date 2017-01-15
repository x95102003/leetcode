#!/usr/bin/env python
# -*- coding: utf-8 -*-

def repeat_substring(test_str):
    """TODO: Docstring for repeat_substring.

    :test_str: TODO
    :returns: TODO

    """
    repeat = ''
    sLen = len(test_str)
    for i in xrange(2, (len(test_str)/2)+1):
        if sLen % i != 0:
            continue
        elif test_str[:i] == test_str[-i:]:
            print test_str[:i]
            repeat = test_str[:i]
            continue
        else:
            continue
    if not repeat:
        if len(set(test_str)) == 1 and len(test_str) != 1:
            return True 
        else:
            return False
        return False
    return True
#print repeat_substring('a')
#print repeat_substring('aba')
#print repeat_substring('abcabcabcabc')
#print repeat_substring('abab')
print repeat_substring('ababab')
