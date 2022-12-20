class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashA = {}
        hashB = {}
        for num in nums1:
            if num in hashA:
                hashA[num] += 1
            else:
                hashA[num] = 1
        for num in nums2:
            if num in hashB:
                hashB[num] += 1
            else:
                hashB[num] = 1
        newHash = {}
        for a in hashA:
            if a in hashB:
                newHash[a] = min(hashA[a], hashB[a])
        resultArray = []
        for b in newHash:
            resultArray += [b]*newHash[b]
        return resultArray
        
        