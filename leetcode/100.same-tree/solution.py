# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.dfs(p, q)
    def dfs(self, p, q):
        if p is None and q is None: return True
        elif p is None: return False
        elif q is None: return False
        else:
            if p.val != q.val: return False
            if p.left is None and q.left is None:
                a = 0
            elif p.left is None: return False
            elif q.left is None: return False
            else:
                if not self.dfs(p.left, q.left): return False
            if p.right is None and q.right is None: a = 0
            elif p.right is None: return False
            elif q.right is None: return False
            else:
                if not self.dfs(p.right, q.right): return False
        return True
