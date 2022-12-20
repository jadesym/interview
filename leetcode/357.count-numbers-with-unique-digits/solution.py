class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is 0: return 1
        cur = self.countNumbersWithUniqueDigits(n-1)
        atm = 9
        for x in range(n - 1):
            atm *= (9-x)
        total = cur + atm
        return total
        