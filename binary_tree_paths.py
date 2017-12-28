#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def binaryTreePaths():
    '''
    :type root: TreeNode
    :rtype: List[str]
    
    Use slice to copy new result prevent the change between left and right.
    in the final element, add to final and join it.
    '''
    def recursive_add(node, result=None, final=None):
        if not node:
            pass
        elif node.left and not node.right:
            node.val = str(node.val)
            result.append(node.val)
            recursive_add(node.left, result[:], final)
        elif not node.left and node.right:
            node.val = str(node.val)
            result.append(node.val)
            recursive_add(node.right, result[:],final)
        elif node.left and node.right:
            node.val = str(node.val)
            result.append(node.val)
            recursive_add(node.left, result[:], final)
            recursive_add(node.right, result[:], final)
        else:
            node.val = str(node.val)
            result.append(node.val)
            final.append('->'.join(result))
    if not root:
        return []
    elif not root.left and not root.right:
        return [str(root.val)]
    else:
        final = []
        result = [str(root.val)]
        recursive_add(root.left, result[:], final)
        recursive_add(root.right, result[:],final)
        return final



