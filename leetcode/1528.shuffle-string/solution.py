class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        indicesToChar = {}
        for i in range(len(s)):
            indicesToChar[indices[i]] = s[i]

        newChars = []
        for index in sorted(indicesToChar.keys()):
            newChars += indicesToChar[index]
        return "".join(newChars)
        