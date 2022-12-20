# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        left = root.left
        right = root.right
        return self.compare(left, right)
    def compare(self, left, right):
        if left is None and right is None: return True
        elif left is None and right is not None: return False
        elif left is not None and right is None: return False
        elif left.val != right.val: return False
        return self.compare(left.left, right.right) and self.compare(left.right, right.left)