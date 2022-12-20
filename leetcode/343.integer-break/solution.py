class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        maximumProduct = {}
        maximumProduct[0] = 0
        maximumProduct[1] = 1
        for x in range(2, n + 1):
            max = 0
            for y in range(1, x):
                diff = x - y
                curMax = diff * maximumProduct[y]
                anotherMax = diff * y
                if curMax > max:
                    max = curMax
                if anotherMax > max:
                    max = anotherMax
            maximumProduct[x] = max
        return maximumProduct[n]

