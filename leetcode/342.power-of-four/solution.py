class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        x = 1
        while x < num:
            x *= 4
            if x > num:
                return False
        return True
                
        
        