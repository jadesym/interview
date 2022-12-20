class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charCount = {}
        for char in s:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
        for index in range(len(s)):
            if charCount[s[index]] == 1:
                return index
        return -1
                
                
        
                