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
    g_idx = 0
    s_idx = 0
    s_len = len(s)
    g_len = len(g)
    g.sort(reverse=True)
    s.sort(reverse=True)
    print g,s
    while True:
	if s_idx >= s_len or g_idx >= g_len: 
	    break
	rem = s[s_idx] - g[g_idx]
	if rem == 0:
	    nums += 1
	    g_idx += 1
	elif rem >= 0:
	    nums += 1
	    g_idx += 1
	else:
	    g_idx += 1
	    continue
	s_idx += 1
    return nums
