class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i = 0
        one = [int(x) for x in version1.split('.')]
        two = [int(y) for y in version2.split('.')]
        while i < len(one) and i < len(two):
            if one[i] < two[i]:
                return -1
            elif one[i] > two[i]:
                return 1
            else:
                i += 1
        while i < len(two):
            if two[i] != 0: return -1
            i += 1
        while i < len(one):
            if one[i] != 0: return 1
            i += 1
        return 0