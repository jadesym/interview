class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        dictionary = {}
        reverse = {}
        for index in range(len(s)):
            curS = s[index]
            curT = t[index]
            if curS in reverse:
                if reverse[curS] != curT: return False
            else:
                reverse[curS] = curT
            if curT in dictionary:
                if dictionary[curT] != curS: return False
            else:
                dictionary[curT] = curS
        return True