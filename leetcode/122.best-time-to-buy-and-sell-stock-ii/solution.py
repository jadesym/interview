class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        elif len(prices) <= 2:
            if prices[1] > prices[0]: return prices[1] - prices[0]
            else: return 0
        maxProfit = 0
        localLow = 0
        localHigh = 0
        ascending = False
        for x in range(len(prices)):
            cur = prices[x]
            if x == 0:
                localLow = cur
                continue
            if x == 1:
                if cur >= localLow:
                    ascending = True
                    localHigh = cur
                else:
                    ascending = False
                    localLow = cur
                    localHigh = cur
                continue
                    
                
            if cur >= localHigh and ascending:
                if x == len(prices) - 1:
                    maxProfit += cur - localLow
                localHigh = cur
            elif cur < localHigh and ascending:
                ascending = False
                maxProfit += localHigh - localLow
                localLow = cur
                localHigh = cur
            elif cur < localLow and not ascending:
                localLow = cur
                localHigh = cur
            elif cur >= localLow and not ascending:
                if x == len(prices) - 1: 
                    maxProfit += cur - localLow
                localHigh = cur
                ascending = True
        return maxProfit
        
            