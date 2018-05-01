# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def largestValues(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    temp_dict = {i:[] for i in xrange(1000)}
    def found_large_num_in_level(node, level):
        if node:
            temp_dict[level].append(node.val)
            found_large_num_in_level(node.left, level+1)
            found_large_num_in_level(node.right, level+1)
        else:
            return
    found_large_num_in_level(root, 0)
    result = []
    for i in temp_dict:
        if not temp_dict[i]:
            break
        temp_dict[i].sort(reverse=True)
        result.append(temp_dict[i][0])
    return result

