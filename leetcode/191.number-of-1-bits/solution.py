class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        temp = n
        while temp > 0:
            ret += temp % 2
            temp = temp // 2
        return ret
            