import heapq

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        pq = []
        for point in points:
            heapq.heappush(pq, (point[0] ** 2 + point[1] ** 2, point))
        return [x[1] for x in heapq.nsmallest(K, pq)]
        