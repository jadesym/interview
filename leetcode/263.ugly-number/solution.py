class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        cur = num
        two = True
        three = True
        five = True
        while cur > 1:
            if two:
                if cur % 2 == 0: cur = cur // 2
                else: two = False
            elif three:
                if cur % 3 == 0: cur = cur // 3
                else: three = False
            elif five:
                if cur % 5 == 0: cur = cur // 5
                else: five = False
            else:
                return False
        return True