# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_unival(root, root.val)
    
    def is_unival(self, node, val):
        if node is None:
            return True
        if node.val != val:
            return False
        return self.is_unival(node.left, val) and self.is_unival(node.right, val)