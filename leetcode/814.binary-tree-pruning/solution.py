# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.getTreeToKeep(root)
    def getTreeToKeep(self, node: TreeNode) -> Optional[TreeNode]:
        if node.left is not None:
            node.left = self.getTreeToKeep(node.left)
        if node.right is not None:
            node.right = self.getTreeToKeep(node.right)

        if node.left is None and node.right is None:
            if node.val == 0: return None
            else: return node
        return node