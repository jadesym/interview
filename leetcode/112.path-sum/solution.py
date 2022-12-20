# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None: 
            return False
        return self.dfs(root, sum, 0)
    def dfs(self, node, sum, sumSoFar):
        if node.left is None and node.right is None:
            return sumSoFar + node.val == sum
        if node.left is not None:
            if self.dfs(node.left, sum, sumSoFar + node.val): return True
        if node.right is not None:
            if self.dfs(node.right, sum, sumSoFar + node.val): return True
        return False
        