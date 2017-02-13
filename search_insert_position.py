#!/usr/bin/env python
# -*- coding: utf-8 -*-

def search_insert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i, v in enumerate(nums):
        if target < v:
            return i
        elif target == v:
            return i
    return len(nums)
