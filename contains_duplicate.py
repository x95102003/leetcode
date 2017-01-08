#!/usr/bin/env python
# -*- coding: utf-8 -*-

def containsDuplicate(nums):
    """TODO: Docstring for containsDuplicate.

    :nums: TODO
    :returns: TODO

    """
    nums = sorted(nums)
    num_l = len(nums)
    if num_l <= 1:
        return False
    for i in xrange(num_l-1):
        if nums[i] == nums[i+1]:
            return True
    return False
