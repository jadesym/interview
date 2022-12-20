class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        curSum = 0
        curNum = num
        while curNum > 0:
            curDigit = curNum % 10
            curSum += curDigit
            curNum = curNum // 10
        if curSum < 10:  return curSum
        else: return self.addDigits(curSum)