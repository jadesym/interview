class Solution(object):
    def isHammingBit(self, x, y):
        return (x % 2) ^ (y % 2) 
        
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        while x > 0 or y > 0:
            distance += self.isHammingBit(x, y)
            x //= 2
            y //= 2
        return distance