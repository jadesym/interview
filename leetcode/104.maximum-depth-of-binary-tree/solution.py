# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)
    def dfs(self, node):
        if node is None: return 0
        if node.left is None and node.right is None: return 1
        left = 0
        right = 0
        if node.left is not None: left = self.dfs(node.left) + 1
        if node.right is not None: right = self.dfs(node.right) + 1
        return max(left, right)