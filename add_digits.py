#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add_digits(num):
    if num < 10:
	return num
    else:
	return add_digits(reduce(lambda x,y:int(x)+int(y), list(str(num))))

print add_digits(1992)
