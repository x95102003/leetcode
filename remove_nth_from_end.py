#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode

    Use Faker root to handle the first element removed,
    send prefix to remove nth element
    """
    def count_from_final_node(prefix, node, n):
        if not node:
            return n-1
        else:
            n = count_from_final_node(node, node.next, n)
            if n == 0:
                if prefix:
                    prefix.next = node.next
            else:
                pass
            return n-1
    if not head:
        return []
    elif not head.next:
        return []
    else:
        faker = ListNode(0)
        faker.next = head
        n = count_from_final_node(faker, head, n)
    return faker.next
