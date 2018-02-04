#!/usr/bin/env python
# -*- coding: utf-8 -*-

def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    count_dict = {'U':-1, 'D':1, 'L':200, 'R':-200}
    result = 0
    for d in moves:
        result += count_dict[d]
    return result == 0

if __name__ == '__main__':
    print judgeCircle('UR')
