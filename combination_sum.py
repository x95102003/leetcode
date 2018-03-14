#!/usr/bin/env python
#-*- coding: utf-8 -*-

def dfs_minus(target, nums, index, temp_path, result):
    '''
    use index to remember the iter location, prevent refound like 2,3,2
    '''
    if target == 0:
        result.append(temp_path)
        return
    for i in xrange(index, len(nums)):
        if nums[i] > target:
            break
        dfs_minus(target-nums[i], nums, i, temp_path+[nums[i]], result)

def combination_sum(candidates, target):
    result = []
    dfs_minus(target, candidates, 0, [], result)   
    return result

if __name__ == '__main__':
    print(combination_sum([2,3,6,7], 7))
