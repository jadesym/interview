class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashA = {}
        hashB = {}
        for num in nums1:
            hashA[num] = True
        for num in nums2:
            hashB[num] = True
        newHash = {}
        for a in hashA:
            if a in hashB:
                newHash[a] = True
        resultArray = []
        for b in newHash:
            resultArray += [b]
        return resultArray