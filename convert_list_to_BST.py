#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def sortedListToBST(self, head):
    """
    :type head: ListNode
    :rtype: TreeNode

    Transform to list first, and split it with half, then add subtree recursively
    """
    def recursive_add(node=None,result=None):
        if not result:
            return None
        half = len(result) / 2
        if node.val >= result[half]:
            node.left = TreeNode(result[half])
            recursive_add(node.left, result[:half])
            recursive_add(node.left, result[half+1:])
        else:
            node.right = TreeNode(result[half])
            recursive_add(node.right, result[:half])
            recursive_add(node.right, result[half+1:])
    slist = []
    while head:
        slist.append(head.val)
        head = head.next
    if not slist:
        return []
    half = len(slist) / 2
    root = TreeNode(slist[half])
    recursive_add(root, slist[:half])
    recursive_add(root, slist[half+1:])
    return root
