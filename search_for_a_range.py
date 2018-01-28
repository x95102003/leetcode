#!/usr/bin/env python
# -*- coding: utf-8 -*-

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(nums)
    if not nums or nums[left] > target or nums[right-1] < target:
        return [-1,-1]
    result = []
    while left <= right:
        half = (left + right)/2
        if nums[half] == target:
            s, e = 0, 0
            end,start = True, True
            while start:
                begin = half - s 
                if begin >= left and nums[begin] == target:
                    s += 1
                else:
                    start = False
            while end:
                fin = half + e
                if fin < right and nums[fin] == target:
                    e += 1
                else:
                    end = False
            result = [half-s + 1, half+e-1]
            break
        elif nums[half] > target:
            if right == half:
                break
            right = half
        else:
            if left == half:
                break
            left = half
    if result:
        return result
    return [-1,-1]
 
if __name__ == '__main__':
     print searchRange([1,2,3,4,4,5,6], 5)
