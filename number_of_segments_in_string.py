#!/usr/bin/env python
# -*- coding: utf-8 -*-

def count_segments(s):
    """TODO: Docstring for count_segments.
        Used loop to calculate the sequence.
    :s: str
    :returns: int 

    """
    result = 0
    prev = 0
    for i in s:
        if prev == 0 and i != ' ':
            result += 1
            prev = 1
        elif i != ' ':
            continue
        else:
            prev = 0
    return result
