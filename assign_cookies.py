#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign_cookies(g, s):
    """TODO: Docstring for assign_cookies.

    :g: TODO
    :s: TODO
    :returns: TODO

    """
    total = sum(s)
    nums = 0
    content = 0
    g = sorted(g, reverse=True)
    print g
    for i in g:
	print i,total,nums
	rem = total - i
	if rem == 0:
	    nums += 1
	    break
	elif rem > 0:
	    total -= i
	    nums += 1
	else:
	    continue
    return nums    
