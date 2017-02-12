#!/usr/bin/env python
# -*- coding: utf-8 -*-

def constructRectangle(self, area):
    """ Use ceil to round the sqrt float up.
    :type area: int
    :rtype: List[int]
    """
    from math import sqrt, ceil
    result = []
    for i in xrange(1, int(ceil(sqrt(area)))+1):
        if area % i == 0:
            division = area/i
            result.append((division, i) if division > i else (i, division))
    return result[0] if len(result) <= 1 else result[-1]
