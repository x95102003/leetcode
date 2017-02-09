#!/usr/bin/env python
# -*- coding: utf-8 -*-

def find_words(self, words):
    """Used dict to hash the value and give the weight for each rows.
    :type words: List[str]
    :rtype: List[str]
    """
    rows = {}
    rows.update({i:0 for i in 'qwertyuiop'})
    rows.update({i:1 for i in 'asdfghjkl'})
    rows.update({i:-10 for i in 'zxcvbnm'})
    result = []
    for word in words:
        tword = word.lower()
        wlen = len(word)
        ans = reduce(lambda x,y: x + y, [rows[i] for i in tword])
        if ans == 0 or ans == wlen or ans == -wlen*10:
            result.append(word)
    return result
