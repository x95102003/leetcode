#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    s = str(x)
    if s[0] == '-':
        v = int(''.join(reversed(s[1:])))
        return 0 if v > 2147483648 else -v
    else:
        v = int(''.join(reversed(s[:])))
        return v if v < 2147483647 else 0

if __name__ == '__main__':
   print reverse(123)
