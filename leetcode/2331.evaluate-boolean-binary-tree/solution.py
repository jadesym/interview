# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            if root.val == 1: return True
            else: return False
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)

        else:
            raise BaseException("Tree is malformed")