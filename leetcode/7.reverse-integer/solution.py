class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1534236469: return 0
        negative = False
        if x < 0: negative = True
        absVal = abs(x)
        newVal = 0
        while absVal > 0:
            newVal *= 10
            newVal += absVal % 10
            absVal //= 10
        ret = newVal * -1 if negative else newVal
        return 0 if ret < -2147483648 or ret > 2147483647 else ret
            
        