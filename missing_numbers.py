#!/usr/bin/env python
# -*- coding: utf-8 -*-

def missing_number(nums):
    """find the missing_number with an array and in the linear time, 

    :nums: list[int]
    :returns: int

    """
    large = max(nums)
    ans = (1+large)*large/2 - sum(nums)
    if 0 not in nums:
        return 0
    elif ans == 0:
        return large + 1
    else:
        return ans
