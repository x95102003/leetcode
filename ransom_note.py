#!/usr/bin/env python
# -*- coding: utf-8 -*-

def canConstruct(ransomNote, magazine):
    if ransomNote in magazine:
	return True
    for l in magazine:
	ransomNote = list(ransomNote)
	if l in ransomNote:
	    ransomNote.remove(l)
	if not ransomNote:
	    return True
    return False
