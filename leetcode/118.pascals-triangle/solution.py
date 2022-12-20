class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        result = [[1]]
        for row in range(1, numRows):
            cur = [1]
            for col in range(1, row):
                upLeft = result[row - 1][col - 1]
                upRight = result[row - 1][col]
                cur.append(upLeft + upRight)
            cur.append(1)
            result.append(cur)
        return result