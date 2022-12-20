"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self.dfs(root)
    def dfs(self, root):
        if root is None: return 0
        maxChild = 0
        for child in root.children:
            maxChild = max(maxChild, self.dfs(child))
        return maxChild + 1