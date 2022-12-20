class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        height = len(grid)
        for rowIndex in range(height):
            row = grid[rowIndex]
            width = len(row)
            for colIndex in range(width):
                val = grid[rowIndex][colIndex]
                
                if val == 1:
                    if rowIndex == 0:
                        perimeter += 1
                        # self.output(grid, rowIndex, colIndex)
                    else:
                        upVal = grid[rowIndex - 1][colIndex]
                        if upVal == 0:
                            perimeter += 1
                            # self.output(grid, rowIndex, colIndex)

                    if rowIndex == height - 1:
                        perimeter += 1
                        # self.output(grid, rowIndex, colIndex)
                    else:
                        downVal = grid[rowIndex + 1][colIndex]
                        if downVal == 0:
                            perimeter += 1
                            # self.output(grid, rowIndex, colIndex)

                    if colIndex == 0:
                        perimeter += 1
                        # self.output(grid, rowIndex, colIndex)
                    else:
                        leftVal = grid[rowIndex][colIndex - 1]
                        if leftVal == 0:
                            perimeter += 1
                            # self.output(grid, rowIndex, colIndex)
                        
                    if colIndex == width - 1:
                        perimeter += 1
                        # self.output(grid, rowIndex, colIndex)
                    else:
                        rightVal = grid[rowIndex][colIndex + 1]
                        if rightVal == 0:
                            perimeter += 1                       
                            # self.output(grid, rowIndex, colIndex)

        return perimeter

    def output(self, grid, row, col):
        print(row, col, grid[row][col])