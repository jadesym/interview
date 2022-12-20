class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        resultStr = []
        indices = []
        chars = []
        for x in range(len(s)):
            char = s[x]
            if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                chars.append(char)
                indices.append(x)
                resultStr.append('_')
            else:
                resultStr.append(char)
        print(indices)
        print(chars)
        for y in range(len(chars) - 1, -1, -1):
            resultStr[indices[len(indices) - y - 1]] = chars[y]
        return ''.join(resultStr)
            
            