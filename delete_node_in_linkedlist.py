#!/usr/bin/env python
# -*- coding: utf-8 -*-

def deleteNode(node):
    """TODO: Docstring for deleteNode.

    :node: TODO
    :returns: No return 
    remove the given node by replacing it with next node 
    """
    node.val = node.next.val
    node.next = node.next.next


