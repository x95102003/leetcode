#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.nt = None

def hasCycle(self, head):
    """
    Use hash to calculate echo node's hash value and in dict to found rapidly. 
    :type head: ListNode
    :rtype: bool
    """
    record = dict()
    while head:
        roothash = hash(head)
        if record.get(roothash):
            return True
        else:
            record[roothash] = True
            head = head.next
    return False
