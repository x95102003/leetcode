#!/usr/bin/env python
# -*- coding: utf-8 -*-

def intersect(nums1, nums2):
    """TODO: Docstring for intersect.

    :nums1: TODO
    :nums2: TODO
    :returns: TODO

    """
    smnums = set(nums1) if len(nums1) > len(nums2) else set(nums2)
    result = []
    print smnums
    for i in smnums:
        smcount = nums1.count(i)
        bgcount = nums2.count(i)
        for j in xrange(smcount) if smcount < bgcount else xrange(bgcount):
            result.append(i)
    return result
print intersect([1, 2, 2, 32, 3, 4, 4], [1, 2, 2, 4, 7, 8, 9, 12, 15])
