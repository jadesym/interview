class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curLow = None
        curMax = None
        profit = 0
        for price in prices:
            # No buy exists yet (None, _)
            if curLow is None:
                curLow = price
                continue
            # No potential sell exists yet (x, None)
            if curMax is None:
                if price > curLow:
                    curMax = price
                elif price < curLow:
                    curLow = price
            # A potential sell exists (x, y)
            else:
                if price > curMax:
                    curMax = price
                elif price < curMax:
                    profit += curMax - curLow
                    curMax = None
                    curLow = price
            print(price, curLow, curMax, profit)

        if curMax is not None:
            return profit + curMax - curLow

        return profit