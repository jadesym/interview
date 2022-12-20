# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        if root is None: return TreeNode(val)
        self.insertDFS(root, val)
        return root
        
    def insertDFS(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self.insertDFS(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self.insertDFS(node.right, val)
        