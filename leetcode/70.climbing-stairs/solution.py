class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        array = [0]*(n+1)
        array[0] = 1
        array[1] = 1
        for x in range(2, n + 1):
            array[x] = array[x - 1] + array[x - 2]
        return array[n]