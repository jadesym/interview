class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        all_xs = 0
        all_ys = {}
        all_zs = 0
        for x in range(len(grid)):
            local_xs = []
            for y in range(len(grid[x])):
                val = grid[x][y]
                if val > 0:
                    all_zs += 1
                if y not in all_ys:
                    all_ys[y] = []
                all_ys[y].append(val)
                local_xs.append(val)
            all_xs += max(local_xs)
        ys_total = sum([max(val_array) for key, val_array in all_ys.items()])
        return all_xs + ys_total + all_zs
        
        