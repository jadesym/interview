class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        sorted_grid = []
        for grid_row in grid:
            sorted_grid.append(sorted(grid_row))

        sum_max = 0
        num_grid_cols = len(sorted_grid[0])
        for i in range(num_grid_cols):
            elems = [grid_row[i] for grid_row in sorted_grid]
            sum_max += max(elems)
        return sum_max