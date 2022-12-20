class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        curWord = ''
        out = ''
        for char in s:
            if char == ' ':
                out += curWord[::-1]
                out += char
                curWord = ''
            else:
                curWord += char
        if len(curWord) > 0:
            out += curWord[::-1]
        return out