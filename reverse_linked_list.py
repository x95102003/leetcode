#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverseList(head):
    """TODO: Docstring for reverseList.

    :head: TODO
    :returns: TODO

    """
    result = []
    if not head:
        return None
    while True:
        if not head:
            break
        else:
            result.append(head.val)
            head = head.next
    result.reverse()
    finalNode = ListNode(result[0])
    prev = finalNode
    for i in result[1:]:
        newNode = ListNode(i)
        prev.next = newNode
        prev = newNode
    return finalNode
