class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        horizontal_max_locals = [[None] * len(grid) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(1, len(grid) - 1):
                horizontal_max_locals[i][j] = max(grid[i][j-1], grid[i][j], grid[i][j+1])
        # print(horizontal_max_locals)
        result = [[None] * (len(grid) - 2) for i in range(len(grid) - 2)]
        for i in range(len(grid) - 2):
            for j in range(len(grid) - 2):
                result[i][j] = max(horizontal_max_locals[i][j+1], horizontal_max_locals[i+1][j+1], horizontal_max_locals[i+2][j+1])
        return result