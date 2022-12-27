# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        nums_digits = []
        self.dfs(root, nums_digits, [])

        sumTotal = 0
        for num_digits in nums_digits:
            actual_num = self.binaryToNum(num_digits)
            sumTotal += actual_num
        return sumTotal

    def binaryToNum(self, digits: List[int]) -> int:
        num = 0
        for digit in digits:
            num *= 2
            num += digit
        return num
    def dfs(self, node: TreeNode, nums_digits: List[List[int]], digitsSoFar: List[int]) -> None:
        if node.left is None and node.right is None:
            nums_digits.append(digitsSoFar + [node.val])
            return
        if node.left is not None:
            self.dfs(node.left, nums_digits, digitsSoFar + [node.val])
        if node.right is not None:
            self.dfs(node.right, nums_digits, digitsSoFar + [node.val])