class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(0,len(nums),2):
            j = i + 1
            freq = nums[i]
            val = nums[j]
            for a in range(freq):
                result.append(val)
        return result
        