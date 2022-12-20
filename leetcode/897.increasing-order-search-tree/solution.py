# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sorted_vals = []
        self.getSortedVals(root, sorted_vals)
        return self.createTree(sorted_vals)
        
    def getSortedVals(self, root, array):
        if root is None: return
        self.getSortedVals(root.left, array)
        array.append(root.val)
        self.getSortedVals(root.right, array)
        
    def createTree(self, vals):
        root = TreeNode(vals[0])
        curNode = root
        for index in range(1, len(vals)):
            curNode.right = TreeNode(vals[index])
            curNode = curNode.right
        return root