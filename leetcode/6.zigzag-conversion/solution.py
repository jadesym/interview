class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ""
        if numRows == 1: return s
        increments = [(numRows - 1 - (curRow % (numRows - 1))) * 2 for curRow in range(numRows)]
        for x in range(numRows):
            cur = ""
            y = x
            while y < len(s):
                cur += s[y]
                increments[x] = (numRows - 1 - (y % (numRows - 1))) * 2
                y += increments[x]
            result += cur
        return result
                
        