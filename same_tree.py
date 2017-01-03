#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isSameTree(p, q):
    """TODO: Docstring for isSameTree.

    :p: TODO
    :q: TODO
    :returns: TODO

    """
    if not p and not q:
        return True
    elif p and q and p.val == q.val:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
        return False
