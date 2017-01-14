#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tohex(num):
    """TODO: Docstring for tohex.

    :num: TODO
    :returns: TODO

    """
    hexd = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f', 0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    result = ''
    while True:
        if 0 > num:
            num = 0xffffffff + num + 1
            print num
        elif num <= 15:
            result = hexd[num] + result
            break
        else:
            result = hexd[num%16] + result
            num /= 16
    return result

print tohex(4294967294)
print tohex(-2)
