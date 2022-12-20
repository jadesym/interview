class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        maxCount = 0
        for x, y in rectangles:
            maxLocal = min(x, y)
            if maxLen < maxLocal:
                maxLen = maxLocal
                maxCount = 1
            elif maxLen == maxLocal:
                maxCount += 1
        return maxCount