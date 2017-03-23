#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDepth(self, root):
    '''
    Check the two subtree whether zero, plus 1 means the root and 
    if one subtree is zero other is minmum path. 
    :type root: TreeNode
    :rtype: int
    '''
    if root:
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return (left + right + 1) if left == 0 or right == 0 else (min(left, right) + 1)
    else:
        return 0
