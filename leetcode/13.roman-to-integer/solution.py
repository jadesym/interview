class Solution(object):
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letterHash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        retInt = 0
        previousVal = letterHash[s[0]]
        previousValCount = 1
        for index in range(1, len(s)):
            curVal = letterHash[s[index]]
            if curVal > previousVal:
                retInt += curVal - previousValCount * previousVal
                previousValCount = 0
            elif curVal == previousVal:
                previousValCount += 1
            else:
                retInt += previousVal * previousValCount
                previousValCount = 1
            previousVal = curVal
        if previousValCount > 0:
            retInt += previousValCount * previousVal
        return retInt
            