#!/usr/bin/env python
# -*- coding: utf-8 -*-

def count_bits(num):
    """
    The next bit would follow the previous answer, [0], ([0+1]), ([0+1], [1+1]) ... follow up
    Use the slice to return copy list and so would not affect the for loop.
    :num: int
    :returns: List[int]

    """
    if num == 0:
        return [0]
    result = []
    result.append(0)
    while True:
        for j in result[:]:
            result.append(j+1)
            if len(result) == num + 1:
                return result
