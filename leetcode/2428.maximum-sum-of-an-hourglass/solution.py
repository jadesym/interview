class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        curMax = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curHourglass = self.calcHourglass(i, j, grid)
                if curHourglass is not None:
                    curMax = max(curHourglass, curMax)
        return curMax

    def calcHourglass(self, i: int, j: int, grid: List[List[int]]) -> Optional[int]:
        m = len(grid)
        n = len(grid[0])
        if i + 2 >= m:
            return None
        if j + 2 >= n:
            return None
        return grid[i][j] + grid[i][j+1] + grid[i][j + 2] \
            + grid[i + 1][j + 1] \
            + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]