# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None: return []
        if root.left is None and root.right is None: return [str(root.val)]
        else:
            paths = []
            if root.left is not None:
                paths += self.dfs(root.left, str(root.val))
            if root.right is not None:
                paths += self.dfs(root.right, str(root.val))
            return paths

    
    def dfs(self, node, inStr):
        paths = []
        if node.left is None and node.right is None:
            paths.append(self.addOn(inStr, node))
        else:
            if node.left is not None:
                paths += self.dfs(node.left, self.addOn(inStr, node))
            if node.right is not None:
                paths += self.dfs(node.right, self.addOn(inStr, node))
        return paths
    
    def addOn(self, inStr, node):
        return inStr + "->" + str(node.val)
        
        