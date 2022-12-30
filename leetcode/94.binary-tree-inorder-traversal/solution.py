# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        nodesSoFar = []
        self.dfs(root, nodesSoFar)
        return nodesSoFar
    
    def dfs(self, node: TreeNode, nodesSoFar: List[TreeNode]) -> None:
        if node.left is not None:
            self.dfs(node.left, nodesSoFar)
        nodesSoFar.append(node.val)
        if node.right is not None:
            self.dfs(node.right, nodesSoFar)
