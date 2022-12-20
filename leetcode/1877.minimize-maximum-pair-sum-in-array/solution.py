class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        maxSum = 0
        for i in range(len(sorted_nums) // 2):
            maxSum = max(maxSum, sorted_nums[i] + sorted_nums[len(sorted_nums) - i - 1])
        return maxSum
        