class Solution(object):
    def getDigits(self, num):
        digits = []
        curNum = num
        while curNum > 0:
            digits.append(curNum % 10)
            curNum //= 10
        return digits

    def digitToNumber(self, digits):
        num = 0
        while len(digits) > 0:
            num *= 10
            num += digits.pop()
        return num
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = self.getDigits(num)

        minSum = 1e99

        sortedDigits = sorted(digits)

        return sortedDigits[0] * 10 + sortedDigits[1] * 10 + sortedDigits[2] + sortedDigits[3]