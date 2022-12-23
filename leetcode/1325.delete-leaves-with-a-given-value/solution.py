# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None: return None
        # left node handling
        if root.left is not None:
            new_left_node = self.removeLeafNodes(root.left, target)
            root.left = new_left_node
        # right node handling
        if root.right is not None:
            new_right_node = self.removeLeafNodes(root.right, target)
            root.right = new_right_node

        # root is leaf
        if root.left is None and root.right is None and root.val == target:
            return None
        return root
        
