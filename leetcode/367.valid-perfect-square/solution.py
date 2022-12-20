class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return self.dfs(0, num, num)
        
    def dfs(self, low, high, val):
        mid = (high + low) // 2
        if low > high: return False
        if mid ** 2 == val: return True
        elif low == high: return False
        elif mid ** 2 < val:
            return self.dfs(mid+1, high, val)
        else:
            return self.dfs(low, mid, val)
        