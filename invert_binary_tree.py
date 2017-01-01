#!/usr/bin/env python
# -*- coding: utf-8 -*-

def invert_binary_tree(root):
    """TODO: Docstring for invert_binary_tree.

    :root: TODO
    :returns: TODO

    """
    if not root:
	return None
    else:
	tmp_node = self.invertTree(root.right)
	root.right = self.invertTree(root.left)
	root.left = tmp_node
    return root 
