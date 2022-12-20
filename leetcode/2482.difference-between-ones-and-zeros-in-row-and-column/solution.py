class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        onesRow = [0 for i in range(m)]
        zerosRow = [0 for i in range(m)]
        onesCol = [0 for i in range(n)]
        zerosCol = [0 for i in range(n)]

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val == 0:
                    zerosRow[i] += 1
                    zerosCol[j] += 1
                elif val == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1
        # print(onesRow, zerosRow)
        # print(onesCol, zerosCol)
        
        new_grid = [[0] * n for j in range(m)]
        for i in range(m):
            for j in range(n):
                new_grid[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        return new_grid