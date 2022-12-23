# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        startMax = -(10 ** 5)
        return self.dfs(root, startMax)
    def dfs(self, node: TreeNode, maxSoFar: int) -> int:
        good_nodes = 0

        cur_node_max = max(maxSoFar, node.val)
        # Handle if root node
        if maxSoFar <= node.val:
            good_nodes += 1
            # print(node.val)

        if node.left is not None:
            good_nodes += self.dfs(node.left, cur_node_max)
        if node.right is not None:
            good_nodes += self.dfs(node.right, cur_node_max)

        return good_nodes

