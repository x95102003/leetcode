#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse_vowel(s):
    """
        A function that takes a string as input and reverse only the vowels of a string.
    :s: str
    :returns: str

    """
    vowels = 'aeiou'
    vowelList = list(vowels + vowels.upper())
    lists = list(s)
    i, j = 0, len(s)-1
    while True:
        if i >= j:
            break
        elif lists[i] in vowelList:
            if lists[j] in vowelList:
                tmp = lists[i]
                lists[i] = lists[j]
                lists[j] = tmp
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            i += 1
    return ''.join(lists)
