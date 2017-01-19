#!/usr/bin/env python
# -*- coding: utf-8 -*-

def climb_stairs(n):
    """TODO: Docstring for climb_stairs.

    :n: TODO
    :returns: TODO

    """
    result = {i:0 for i in xrange(1, n+1)}
    result.update({0:1})
    result.update({-1:0})
    for i in xrange(1, n+1):
        result[i] = result[i-1] + result[i-2]

    return result[n]eturn 
