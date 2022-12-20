# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return (self.dfs(root, p, q))[2]
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    def dfs(self, node, p, q):
        found = []
        if node is None: return []

        if node == p: found.append(p)
        if node == q: found.append(q)
        if node.left is not None:
            sol = self.dfs(node.left, p, q)
            if len(sol) == 3: return sol
            elif len(sol) == 2: return sol + [node]
            else: found += sol
        if node.right is not None:
            sol = self.dfs(node.right, p, q)
            if len(sol) == 3: return sol
            elif len(sol) == 2: return sol + [node]
            else: found += sol
        if len(found) == 2: 
            print(found)
            return found + [node]
        else:
            print(found)
            return found