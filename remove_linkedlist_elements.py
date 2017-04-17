#!/usr/bin/env python
# -*- coding: utf-8 -*-

def removeElements(self, head, val):
    """
    Remove the duplicate elements in list by change their link. 
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    root = head
    prev = None
    while head:
        next = head.next
        if head.val == val:
            if prev == None:
                root = next
                prev = None
                head = head.next
                continue
            else:
                prev.next = next
                head = head.next
        else:
            prev = head
            head = head.next
    return root
