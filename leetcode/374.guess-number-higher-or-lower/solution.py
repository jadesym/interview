# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binSearch(0, n + 1)
        
    def binSearch(self, low, high):
        mid = (low + high) // 2
        if guess(mid) == -1:
            return self.binSearch(0, mid)
        elif guess(mid) == 1:
            return self.binSearch(mid, high)
        else:
            return mid