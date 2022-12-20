class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        bestDiff = 0
        if len(prices) <= 1: return bestDiff
        localLow = prices[0]
        lastPrice = prices[0]
        for index in range(1, len(prices)):
            curPrice = prices[index]
            if curPrice > lastPrice:
                if curPrice - localLow > bestDiff:
                    bestDiff = curPrice - localLow
            elif curPrice < lastPrice:
                if curPrice - localLow > bestDiff:
                    bestDiff = curPrice - localLow
                if curPrice < localLow:
                    localLow = curPrice
            lastPrice = curPrice
        if lastPrice - localLow > bestDiff:
            bestDiff = lastPrice - localLow
        return bestDiff
            