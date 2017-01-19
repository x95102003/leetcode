#!/usr/bin/env python
# -*- coding: utf-8 -*-

def hamming_weight(n):
    """TODO: Docstring for hamming_weight.

    :n: TODO
    :returns: TODO

    """
    print bin(n)
    return bin(n).count('1')

print hamming_weight(11)
