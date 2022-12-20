class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        minTime = 0
        for i in range(len(points) - 1):
            pointA = points[i]
            pointB = points[i + 1]
            localTime = self.timeBetweenPoints(pointA, pointB)
            # print(localTime)
            minTime += localTime
        return minTime
    
    def timeBetweenPoints(self, pointA, pointB):
        aX, aY = pointA
        bX, bY = pointB
        xDiff = abs(aX - bX)
        yDiff = abs(aY - bY)
        return max(xDiff, yDiff)

