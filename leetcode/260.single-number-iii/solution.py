class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        
        bit = xor & ~(xor - 1)
        
        result = [0, 0]
        for num in nums:
            if num & bit > 0:
                result[0] ^= num
            else:
                result[1] ^= num
        return result
        