#!/usr/bin/env python
# -*- coding: utf-8 -*-

def delete_duplicates(head):
    """TODO: Docstring for delete_duplicates.

    :head: TODO
    :returns: TODO

    """
    record = []
    while True:
        if not head:
            break
        else:
            if head.val in record:
                head = head.next
            else:
                record.append(head.val)
                head = head.next
    head = ListNode(0)
    prev = head
    for i in record:
        newNode = ListNode(i)
        prev.next = newNode
        prev = newNode
    return head.next
        
