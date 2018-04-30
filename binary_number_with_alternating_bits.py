#!/usr/bin/env python
# -*- coding: utf-8 -*-

def hasAlternatingBits(n):
        """
        :type n: int
        :rtype: bool
        """
        sb = bin(n)[2:]
        result = int(sb[0])
        for v in sb[1:]:
            v = int(v)
            if result ^ v:
                result = v
            else:
                break
        else:
            return True
        return False

if __name__ == '__main__':
    print hasAlternatingBits(5)
