class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        digits = set([int(x) for x in n])
        return max(digits)
        