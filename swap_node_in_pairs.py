#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def swap_pairs(head):
    """TODO: Docstring for swap_pairs.
        Check every node and its child and then replace it by its child of child
    :head: ListNode 
    :returns: ListNode 

    """ 
    node = head
    while head:
        if head and head.next:
            head.next.val ^= head.val
            head.val ^= head.next.val
            head.next.val ^= head.val
            head = head.next.next
        else:
            break
    return node
