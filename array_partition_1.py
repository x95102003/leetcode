#!/usr/bin/env python
# -*- coding: utf-8 -*-

def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s_nums = sorted(nums)
    result = 0
    for i in xrange(0, len(s_nums), 2):
        result += s_nums[i]
    return result

if __name__ == '__main__':
    print arrayPairSum([1,4,3,2])
