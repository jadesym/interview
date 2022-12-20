class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        curVal = 1
        while curVal < n:
            if curVal == n: return True
            elif curVal > n: return False
            else:
                curVal *= 2
        if curVal == n: return True
        else: return False