# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        first_leaves = []
        self.getLeaves(root1, first_leaves)
        second_leaves = []
        self.getLeaves(root2, second_leaves)
        return first_leaves == second_leaves
    
    def getLeaves(self, root, leafList):
        if root is None: return
        if root.left is None and root.right is None:
            leafList.append(root.val)
        self.getLeaves(root.left, leafList)
        self.getLeaves(root.right, leafList)
        