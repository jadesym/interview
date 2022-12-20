class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        additions = 0
        lastNum = nums[0]
        for i in range(1, len(nums)):
            curNum = nums[i]
            newNumRequired = lastNum + 1
            # print(i, curNum, lastNum, newNumRequired)
            if curNum <= lastNum:
                localAdditions = newNumRequired - curNum
                additions += localAdditions
            lastNum = max(newNumRequired, curNum)
        return additions
