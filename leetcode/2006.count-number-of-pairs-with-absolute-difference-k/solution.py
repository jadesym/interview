class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numCount = dict()
        for num in nums:
            if num not in numCount: numCount[num] = 0
            numCount[num] += 1

        runningCount = 0
        for num, count in numCount.items():
            if num + k in numCount: runningCount += count * numCount[num + k]
            if num - k in numCount: runningCount += count * numCount[num - k]
        return runningCount // 2