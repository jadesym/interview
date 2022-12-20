class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # result = [[0] * n for i in range(m)]
        rowIncrements = {}
        colIncrements = {}
        for rowToIncrement, colToIncrement in indices:
            if rowToIncrement not in rowIncrements:
                rowIncrements[rowToIncrement] = 0
            if colToIncrement not in colIncrements:
                colIncrements[colToIncrement] = 0
            rowIncrements[rowToIncrement] += 1
            colIncrements[colToIncrement] += 1

        oddCounts = 0
        for i in range(m):
            for j in range(n):
                curRowIncrement = rowIncrements[i] if i in rowIncrements else 0
                curColIncrement = colIncrements[j] if j in colIncrements else 0
                if (curRowIncrement + curColIncrement) % 2 == 1: oddCounts += 1
        return oddCounts
        