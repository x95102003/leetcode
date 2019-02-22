# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.store = []
        tmp = [root]
        while len(tmp) != 0:
            n = tmp.pop(0)
            self.store.append(n.val)
            if n.left:
                tmp.append(n.left)
            if n.right:
                tmp.append(n.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        self.store.append(v)
        return self.store[len(self.store)/2 - 1]

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.store
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
