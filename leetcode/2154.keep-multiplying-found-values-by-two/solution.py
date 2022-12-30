class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        curNum = original
        num_set = set(nums)
        while curNum in num_set:
            curNum *= 2
        return curNum