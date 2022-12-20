from math import factorial

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDigits = {}
        for num in nums:
            if num in numDigits: numDigits[num] += 1
            else: numDigits[num] = 1
        pairs = 0
        for num, count in numDigits.items():
            if count == 1: pass
            else:
                pairs += factorial(count) / factorial(count - 2) / 2
        return pairs        