class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        accountSums = [sum(x) for x in accounts]
        return max(accountSums)
        
        