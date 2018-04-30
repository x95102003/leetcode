#!/usr/bin/env python
#-*- coding: utf-8 -*-

def dfs_append(nums, lenth, path, result):
    """
    Use dfs and path to check all ele is chosen
    """
    if len(path) == lenth:
        result.append(path)
        return
    for i in xrange(0, lenth):
        if nums[i] not in path:
            dfs_append(nums, lenth, path+[nums[i]], result)
    
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    if not len(nums):
        return []
    lenth = len(nums)
    dfs_append(nums, lenth, [], result)
    return result

if __name__ == '__main__':
    print(permute([1,2,3]))