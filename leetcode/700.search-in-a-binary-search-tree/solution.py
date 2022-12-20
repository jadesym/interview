# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None: return None
        elif root.val == val:
            return root
        elif root.val < val:
            if root.right is None: return None
            return self.searchBST(root.right, val)
        else:
            if root.left is None: return None
            return self.searchBST(root.left, val)
            
            
        