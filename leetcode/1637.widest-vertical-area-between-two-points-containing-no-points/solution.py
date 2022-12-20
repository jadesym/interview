class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xPoints = sorted(set([x for [x, y] in points]))
        maxWidth = 0
        curX = xPoints[0]
        for index in range(1, len(xPoints)):
            curWidth = xPoints[index] - curX
            if curWidth >= maxWidth:
                maxWidth = curWidth
            curX = xPoints[index]
        return maxWidth