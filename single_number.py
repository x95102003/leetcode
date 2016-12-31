#!/usr/bin/env python
# -*- coding: utf-8 -*-

def single_number(nums):
    """TODO: Docstring for single_number.

    :nums: TODO
    :returns: TODO

    """ 
    r = 0
    for i in nums:
        r = r ^ i
    return r
