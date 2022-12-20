# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        return self.dfs(0, n)
        """
        :type n: int
        :rtype: int
        """
        
    def dfs(self, low, high):
        mid = (low + high) // 2
        if low >= high: return high
        if isBadVersion(mid): return self.dfs(low, mid)
        else: return self.dfs(mid + 1, high)
        