#!/usr/bin/env python
# -*- coding: utf-8 -*-
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i, j = 0, 1
    while nums:
        if i == (len(nums) -1):
            break
        elif nums[i] == nums[j]:
            del nums[j]
        else:
            i += 1
            j = i+1

if __name__ == "__main__":
    nums = [1,2,2]
    removeDuplicates(nums)
    print nums
