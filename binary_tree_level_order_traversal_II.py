#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    def _addstage(node, i, result):
        if node:
            result.append([])
            result[i] += [node.val]
            i += 1
            _addstage(node.left, i, result)
            _addstage(node.right, i, result)
            return i

    result = [] 
    _addstage(root, 0, result)
    result.reverse()
    return [s for s in result if s]
