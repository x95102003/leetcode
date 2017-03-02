#!/usr/bin/env python
# -*- coding: utf-8 -*-

def detectCapitalUse(self, word):
    """
    :type word: str
    :rtype: bool
    """
    if word.isupper() or word.islower():
        return True
    elif word[0].isupper():
        if word[1:].islower():
            return True
        else:
            return False
    else:
        return False
