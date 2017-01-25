#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rob(nums):
    """TODO: Docstring for rob.
    Use a result array to calculate the max of previous element and add this element to it.
    :nums: List[int]
    :returns: int

    """
    lent = len(nums)
    if not nums:
        return 0
    result = [0] * lent
    for i in xrange(lent):
        if (i - 2) < 0:
            result[i] = nums[i]
        else:
            if (i - 3) >= 0:
                result[i] = max(result[:i-1]) + nums[i]
            else:
                result[i] = result[i-2] + nums[i]
    return max(result)
