#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sumOfLeftLeaves(root):
    """TODO: Docstring for sumOfLeftLeaves.

    :root: TODO
    :returns: TODO

    """
    if not root:
	return 0
    if root.left and not root.left.left and not root.left.right:
	return root.left.val + self.sumOfLeftLeaves(root.right)
    else:
	return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
