# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        root1_array = self.getUnsortedArray(root1)
        root2_array = self.getUnsortedArray(root2)
        return sorted(root1_array + root2_array)
    def getUnsortedArray(self, root: TreeNode):
        unsorted_array = []
        self.dfs(root, unsorted_array)
        return unsorted_array
    def dfs(self, node: TreeNode, array: List[int]) -> None:
        if node is None: return
        array.append(node.val)
        self.dfs(node.left, array)
        self.dfs(node.right, array)