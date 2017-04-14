#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        tmp = self.q[-1]
        self.q = self.q[:-1]
        return tmp

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return None
        return self.q[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push("a")
obj.push("c")
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print param_2, param_3, param_4
