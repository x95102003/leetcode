#!/usr/bin/env python
# -*- coding: utf-8 -*-

def convert_to_base7(num):
    """
    :type num: int
    :rtype: str
    """
    result = ''
    sign = ''
    if num < 0:
        sign = '-'
        num = abs(num)
    while num >= 7:
        result = str(num % 7) + result
        num /= 7
    result = str(num) + result

    return sign + result

print convert_to_base7(1001)
print convert_to_base7(100)
print convert_to_base7(-7)
print convert_to_base7(7)
print convert_to_base7(1)

        
