import math

class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        totals = []
        for query in queries:
            pointCount = 0
            for point in points:
                y2, x2, r = query
                y1, x1 = point
                
                if math.sqrt(abs(y2 - y1)**2 + abs(x2 - x1)**2) <= r:
                    pointCount += 1
            totals.append(pointCount)
        return totals