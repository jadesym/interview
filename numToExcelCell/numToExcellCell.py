# Link: https://leetcode.com/problems/excel-sheet-column-title/
# Description: Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# Example
#    1 -> A
#    2 -> B
#    3 -> C
#    ...
#    26 -> Z
#    27 -> AA
#    28 -> AB 

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
