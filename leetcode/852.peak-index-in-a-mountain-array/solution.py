class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        maxVal = 0
        maxIndex = 0
        for i in range(len(A)):
            a = A[i]
            if a > maxVal:
                maxVal = a
                maxIndex = i
        return maxIndex
        