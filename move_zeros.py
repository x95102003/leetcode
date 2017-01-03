#!/usr/bin/env python
# -*- coding: utf-8 -*-

def move_zeros(nums):
    """TODO: Docstring for move_zeros.

    :nums: TODO
    :returns: TODO

    """
    num = nums.count(0)
    for _ in xrange(num):
	nums.remove(0)
	nums.append(0)

