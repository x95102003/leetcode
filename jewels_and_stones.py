#!/usr/bin/env python
# -*- coding: utf-8 -*-

def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    from collections import Counter
    count_dict = Counter(S)
    return sum([count_dict[s] for s in J])

if __name__ == '__main__':
    print numJewelsInStones('aA', 'aAAASSSS')
