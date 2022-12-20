class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        twos = 0
        fives = 0
        twoExponent = 1
        fiveExponent = 1
        while twoExponent <= n:
            twoExponent *= 2
            twos += n // twoExponent
        while fiveExponent <= n:
            fiveExponent *= 5
            fives += n // fiveExponent
        return min(twos, fives)
        