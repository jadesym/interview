class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum((n>>i&1)<<(31-i) for i in range(32))
