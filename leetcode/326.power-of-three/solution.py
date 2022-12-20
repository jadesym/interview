class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        curVal = 1
        while curVal < n:
            if curVal == n: return True
            elif curVal > n: return False
            else: curVal *= 3
        if curVal == n: return True
        return False