#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_binary_watch(num):
    """TODO: Docstring for read_binary_watch.

    :num: TODO
    :returns: TODO

    """
    import itertools
    h = [10, 20, 40, 80]
    m = [1, 2, 4, 8, 16, 32]
    result = set()
    for i in itertools.combinations(h + m, num):
        hour,mit = 0, 0
        for time in list(i):
            tmph = time % 10
            if tmph == 0:
                hour += time / 10
            else:
                mit += time
        if  hour < 12 and mit < 60:
            result.add('{0}:{1:02d}'.format(hour, mit))
    return list(result)
print read_binary_watch(2)
