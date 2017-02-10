#!/usr/bin/env python
# -*- coding: utf-8 -*-

def findMaxConsecutiveOnes(self, nums):
    """ Use the mx to record max and nx to add if it is 1.
    :type nums: List[int]
    :rtype: int
    """
    mx = 0
    nx = 0
    for i in nums:
        if i == 1:
            nx += 1
        else:
            mx = nx if mx < nx else mx
            nx = 0
    mx = nx if mx < nx else mx
    return mx
