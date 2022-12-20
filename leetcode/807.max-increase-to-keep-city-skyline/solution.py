class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        maxX = []
        maxY = []
        for row in grid:
            maxY.append(max(row))
        numColumns = len(grid[0])
        numRows = len(grid)
        for columnIndex in range(numColumns):
            columnLocalMax = 0
            for rowIndex in range(numRows):
                columnLocalMax = max(columnLocalMax, grid[rowIndex][columnIndex])
            maxX.append(columnLocalMax)

        increase = 0    
        for x in range(numRows):
            newGridRow = []
            for y in range(numColumns):
                newHeight = min(maxX[x], maxY[y])
                increase += newHeight - grid[x][y]
        return increase
