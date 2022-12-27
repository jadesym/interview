import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestLow = sys.maxsize
        highestProfit = 0
        for price in prices:
            if price < lowestLow: lowestLow = price
            if price > lowestLow:
                highestProfit = max(highestProfit, price - lowestLow)
        return highestProfit
            
            

            
            

