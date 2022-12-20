class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        array = [0]*(rowIndex+1)
        array[0] = 1
        for x in range(rowIndex + 1):
            for y in range(x,0, -1):
                array[y] = array[y] + array[y-1]
        return array
                
        