class Solution:
    # [0, 0, 1, 1]
    # [1, 0, 1, 0]
    # [1, 1, 0, 0]
    #
    # 24 + 8 + 4 + 3
    # [1, 1, 1, 1]
    # [1, 0, 0, 1]
    # [1, 1, 1, 1]
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[0])):
                    grid[i][j] ^= 1
        for j in range(len(grid[0])):
            colCount = 0
            for i in range(len(grid)):
                colCount += grid[i][j]
            if colCount <= len(grid) // 2:
                for i in range(len(grid)):
                    grid[i][j] ^= 1

        # for row in grid:
        #     print(row)
        score = 0
        for row in grid:
            rowScore = 0
            for j in range(len(row)):
                rowScore += (row[j]) * (2 ** (len(row) - j - 1))
            score += rowScore
            # print(rowScore)
        return score
