class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sHash = {}
        tHash = {}
        for sChar in s:
            if sChar in sHash:
                sHash[sChar] += 1
            else:
                sHash[sChar] = 1
        for tChar in t:
            if tChar in tHash:
                tHash[tChar] += 1
            else:
                tHash[tChar] = 1
        if len(sHash) is not len(tHash): return False
        else:
            for key in sHash:
                if key not in tHash: return False
                if sHash[key] != tHash[key]: return False
        return True