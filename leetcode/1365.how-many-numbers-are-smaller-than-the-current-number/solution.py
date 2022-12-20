class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numCounts = {}
        for num in nums:
            if num in numCounts: numCounts[num] += 1
            else: numCounts[num] = 1
        currentNumsLess = 0
        numsLess = {}
        for num in sorted(numCounts.keys()):
            numsLess[num] = currentNumsLess
            currentNumsLess += numCounts[num]
        
        return [numsLess[num] for num in nums]
        