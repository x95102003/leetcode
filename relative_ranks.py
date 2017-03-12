#!/usr/bin/env python
# -*- coding: utf-8 -*-

def findRelativeRanks(self, nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    snums = sorted(nums, reverse=True)
    honor = {0:'Gold Medal', 1:'Silver Medal', 2:'Bronze Medal'} 
    result = []
    for v in nums:
        idx = snums.index(v)
        if idx in honor:
            result.append(honor[idx])
        else:
            result.append(str(idx+1))
    return result
