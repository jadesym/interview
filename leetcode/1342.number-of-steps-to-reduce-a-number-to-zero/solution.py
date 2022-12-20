class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        curNum = num
        while curNum > 0:
            if curNum % 2 == 0:
                curNum //= 2
                steps += 1
            else:
                curNum -= 1
                steps += 1
        return steps
            
        