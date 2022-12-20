# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        if self.dfs(root) is None: return False
        return True
    
    def dfs(self, node):
        if node is None: return 0
        leftVal = self.dfs(node.left)
        rightVal = self.dfs(node.right)
        if leftVal is None or rightVal is None: return None
        if leftVal > rightVal + 1 or leftVal + 1 < rightVal:
            return None
        else:
            return max(leftVal, rightVal) + 1
        