#!/usr/bin/env python
# -*- coding: utf-8 -*-

def generate(numRows):
    """TODO: Docstring for generate.

    :numRow: int
    :returns: List[List[int]]

    """
    result = []
#    if numRows == 0:
#        return []
#    result.append([1])
    for i in xrange (numRows):
        tmp = []
        for j in xrange(i+1):
            if j == 0 or j == i + 1:
                tmp.append(1)
            elif j == i:
                tmp.append(1)
            else:
                tmp.append(result[i-1][j] + result[i-1][j-1])
        result.append(tmp)
    return result

print generate(0)
print generate(4)
