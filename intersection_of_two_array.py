#!/usr/bin/env python
# -*- coding: utf-8 -*-

def intersection(nums1, nums2):
    """TODO: Docstring for intersection.
    I thought it would not implement set function.
    :nums1: TODO
    :nums2: TODO
    :returns: TODO

    result = []
    idx = 0
    for i in nums1:
	if i in nums2 and i not in result:
	    result.append(i)
    return result"""
    return list(set(nums1)&set(nums2))
