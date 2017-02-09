#!/usr/bin/env python
# -*- coding: utf-8 -*-

def find_complement(self, num):
    """Get the complement of number by using the '1' of len(num) minus num
    :type num: int
    :rtype: int
    """
    d = bin(num)[2:]
    if num >= 0:
        return int('1' * len(d), 2) - num
