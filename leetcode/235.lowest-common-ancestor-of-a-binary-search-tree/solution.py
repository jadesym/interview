# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, node, tuplePassed):
        if root is None:
            return None
        elif root is node:
            return tuple(tuplePassed + (node,))
        else:
            nextTuple = tuple(tuplePassed + (root,))
            if root.left is not None:
                retTuple = self.dfs(root.left, node, nextTuple)
                if retTuple is not None: return retTuple
            if root.right is not None:
                retTuple = self.dfs(root.right, node, nextTuple)
                if retTuple is not None: return retTuple
            return None
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pPath = self.dfs(root, p, tuple())
        qPath = self.dfs(root, q, tuple())
        lastAncestor = root
        index = 0
        while index < len(pPath) and index < len(qPath):
            pAncestor = pPath[index]
            qAncestor = qPath[index]
            if pAncestor is not qAncestor:
                break
            lastAncestor = pAncestor
            index += 1
        return lastAncestor
            