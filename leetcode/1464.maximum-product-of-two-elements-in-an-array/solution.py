class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return max([(sorted_nums[i] - 1) * (sorted_nums[i + 1] - 1) for i in range(len(nums) - 1)])