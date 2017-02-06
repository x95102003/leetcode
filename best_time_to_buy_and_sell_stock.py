#!/usr/bin/env python
# -*- coding: utf-8 -*-

def max_profit(prices):
    """ Appending the first element, and compare next then put smaller element into list. 
    :prices: List[int]
    :returns: int

    """
    tmp_result = []
    max_value = 0
    if not prices:
        return 0
    tmp_result.append(prices[0])
    for v in prices[1:]:
        tmp_max = v - tmp_result[0]
        if tmp_max > max_value:
            max_value = tmp_max
        if tmp_result[0] > v:
            tmp_result[0] = v
    return max_value
print max_profit([7, 1, 5, 3, 6, 4])
print max_profit([7, 6, 4, 3, 1])           
print max_profit([2, 1, 2, 0, 1])
