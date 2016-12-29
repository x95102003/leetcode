# -*- coding: utf-8 -*-

def hammingDistance(x, y):
    return diff = bin(x ^ y)[2:].count('1')

print hammingDistance(4,1)

