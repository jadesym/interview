# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, nums, low, high):
        maxIndex = None
        maxVal = 0
        for index in range(low, high):
            if nums[index] >= maxVal:
                maxVal = nums[index]
                maxIndex = index
        if maxIndex is None:
            return None

        maxNode = TreeNode(maxVal)
        leftNode = self.dfs(nums, low, maxIndex)
        maxNode.left = leftNode
        rightNode = self.dfs(nums, maxIndex + 1, high)
        maxNode.right = rightNode
        return maxNode
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.dfs(nums, 0, len(nums))