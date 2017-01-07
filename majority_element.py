#!/usr/bin/env python
# -*- coding: utf-8 -*-

def majority_element(nums):
    """TODO: Docstring for majority_element.

    :nums: TODO
    :returns: TODO

    """
    nums = sorted(nums)
    ind = len(nums)/2
    return nums[ind]
