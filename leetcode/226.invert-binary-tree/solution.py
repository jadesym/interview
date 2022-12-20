# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        return root
    
    def dfs(self, node):
        if node is None:
            return
        else:
            self.dfs(node.left)
            self.dfs(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp
            

        