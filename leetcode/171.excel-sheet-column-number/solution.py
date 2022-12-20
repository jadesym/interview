class Solution(object):
    def convertToNum(self, letter):
        return ord(letter) - 64
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        for char in s:
            val *= 26
            val += self.convertToNum(char)
        return val    
    