#!/usr/bin/env python
# -*- coding: utf-8 -*-

def containsNearbyDuplicate(self, nums, k):
    """
    Use dict to store the index of same and check it.
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    nlen = len(nums)
    dic = {}
    if nlen == 0 or k == 0:
        return False
    for i, e in enumerate(nums):
        if e in dic:
            for idx in dic[e]:
                if abs(i - idx) <= k:
                    return True
            dic[e].append(i)
        else:
            dic.update({e:[i]})
    return False
