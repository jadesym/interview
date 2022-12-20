class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = ""
        while n > 0:
            n -= 1
            remainder =  n % 26
            string += chr(remainder + 65)
            n -= remainder
            n //= 26
        return string[::-1]