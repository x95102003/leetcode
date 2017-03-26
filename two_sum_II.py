#!/usr/bin/env python
# -*- coding: utf-8 -*-

def twoSum(self, numbers, target):
    """
    The numbers is sorted and we can use hash to find whether the minus value exists.
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {v:i for i, v in enumerate(numbers)}
    for i, v in enumerate(numbers):
        r = d.get(target-v)
        if r:
            return [i+1, r+1]
