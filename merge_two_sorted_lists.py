#!/usr/bin/env python
# -*- coding: utf-8 -*-

def merge_two_lists(l1, l2):
    """TODO: Docstring for merge_two_lists.

    :l1: TODO
    :l2: TODO
    :returns: TODO

    """
    finalNode = ListNode(0)
    head = finalNode
    while True:
        if not l1 and not l2:
            break
        elif not l1:
            finalNode.next = l2
            finalNode = finalNode.next
            l2 = l2.next
        elif not l2:
            finalNode.next = l1
            finalNode = finalNode.next
            l1 = l1.next
        else:
            if l1.val > l2.val:
                finalNode.next = l2
                finalNode = finalNode.next
                l2 = l2.next
            else:
                finalNode.next = l1
                finalNode = finalNode.next
                l1 = l1.next
    return head.next
