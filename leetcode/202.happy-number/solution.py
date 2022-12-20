class Solution(object):
    def reduce(self, n):
        sum = 0
        valSoFar = n
        while valSoFar > 0:
            curVal = valSoFar % 10
            sum += curVal ** 2
            valSoFar = valSoFar // 10
        return sum
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = {}
        
        curVal = n
        while curVal != 1:
            if curVal in visited: return False
            visited[curVal] = True
            curVal = self.reduce(curVal)
        return True