#!/usr/bin/env python
# -*- coding: utf-8 -*-

def next_greater_element(self, findNums, nums):
    """ Compare the next elemnet and if list 
    then return list[0] else not found return -1

    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []
    for i in findNums:
        large = [j for j in nums[nums.index(i):] if j > i]
        result.append(-1 if not large else large[0])
    return result
