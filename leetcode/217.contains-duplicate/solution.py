class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numHash = {}
        for num in nums:
            if num in numHash: return True
            else: numHash[num] = True
        return False