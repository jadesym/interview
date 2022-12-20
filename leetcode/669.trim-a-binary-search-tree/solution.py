# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None: return None
        return self.removeNode(root, L, R)

    def removeNode(self, root, L, R):
        if root.left is not None:
            root.left = self.removeNode(root.left, L, R)
        if root.right is not None:
            root.right = self.removeNode(root.right, L, R)           

        if root.val < L:
            if root.right is None:
                return None
            else:
                return root.right
        elif root.val > R:
            if root.left is None:
                return None
            else:
                return root.left
        else:
            return root

        
            
        