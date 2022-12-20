class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        curWord = []
        for index in range(len(s) - 1, -1, -1):
            if s[index] == ' ' and len(curWord) == 0: continue
            elif s[index] == ' ': return len(curWord)
            curWord.append(s[index])
        return len(curWord)
            
        