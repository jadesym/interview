class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sumList = []
        curSum = 0
        for num in nums:
            curSum += num
            sumList.append(curSum)
        return sumList