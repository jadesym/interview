class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        buckets = {}
        for index, num in enumerate(nums):
            if num in buckets and index - buckets[num] <= k: return True
            buckets[num] = index
        return False