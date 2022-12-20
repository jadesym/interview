class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numHash = {}
        for num in nums:
            if num in numHash:
                numHash[num] += 1
            else:
                numHash[num] = 1
        maxCount = 0
        maxNumber = 0
        for number in numHash:
            if numHash[number] > maxCount:
                maxNumber = number
                maxCount = numHash[number]
        return maxNumber