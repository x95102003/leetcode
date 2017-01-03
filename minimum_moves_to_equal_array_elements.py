#!/usr/bin/env python
# -*- coding: utf-8 -*-

def minMoves(nums):
    """
 	calc difference between pairs and it would increse that related its numbers
    """
    nums.sort(reverse=True)
    diff = []
    moves = 0
    for idx in xrange(len(nums)-1):
	diff.append(nums[idx] - nums[idx+1])
    for idx, v in enumerate(diff):
	moves += (idx + 1) * v
    return moves
