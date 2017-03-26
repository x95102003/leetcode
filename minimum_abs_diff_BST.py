#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getMinimumDifference(self, root):
    """
    Get the tree list first, then sorted and find each difference O(nlogn)=2n+nlogn
    :type root: TreeNode
    :rtype: int
    """
    def _recur_append(root, result):
        if root:
            result.append(root.val)
            _recur_append(root.left, result)
            _recur_append(root.right, result)
        else:
            return None
    result = []
    _recur_append(root, result)
    result.sort()
    min_diff = 10000000
    for i in xrange(len(result) - 1):
        diff = result[i+1] - result[i]
        if diff < min_diff:
            min_diff = diff
        else:
            continue
    return min_diff
