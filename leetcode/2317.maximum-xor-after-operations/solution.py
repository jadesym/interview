class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        runningOR = nums[0]
        for i in range(1, len(nums)):
            runningOR |= nums[i]
        return runningOR
        