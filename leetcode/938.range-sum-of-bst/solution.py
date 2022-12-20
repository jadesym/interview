from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        return self.dfs(root, L, R)
    def dfs(self, node, L, R):
        if node is None: return 0
        if node.val < L:
            return self.dfs(node.right, L, R)
        elif node.val == L:
            return node.val + self.dfs(node.right, L, R)
        elif node.val > L and node.val < R:
            return self.dfs(node.left, L, R) + node.val + self.dfs(node.right, L, R)
        elif node.val == R:
            return self.dfs(node.left, L, R) + node.val
        else:
            return self.dfs(node.left, L, R)
            
        