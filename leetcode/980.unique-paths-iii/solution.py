from typing import Set
from copy import deepcopy

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        resultPaths = []
        walkable_count = 0
        startCoords = None
        endCoords = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                value = grid[i][j]
                if value != -1:
                    walkable_count += 1
                if value == 1:
                    startCoords = (i, j)
                elif value == 2:
                    endCoords = (i, j)

        self.dfs(walkable_count, [startCoords], set([startCoords]), grid, resultPaths)
        return len(resultPaths)

    def dfs(self, walkable_count: int, curPath: List[tuple[int, int]], curPathSet: Set[tuple[int, int]], original_grid: List[List[int]], resultPaths: List[tuple[int, int]]):
        m = len(original_grid)
        n = len(original_grid[0])

        if len(curPath) == walkable_count:
            resultPaths.append(curPath)
            return
        nextSteps = []
        curI, curJ = curPath[len(curPath) - 1]
        tempNextSteps = []

        if curI < m - 1:
            tempNextSteps.append((curI + 1, curJ))
        if curI > 0:
            tempNextSteps.append((curI - 1, curJ))
        if curJ < n - 1:
            tempNextSteps.append((curI, curJ + 1))
        if curJ > 0:
            tempNextSteps.append((curI, curJ - 1)) 
       
        for i, j in tempNextSteps:
            if (i, j) in curPathSet:
                continue

            nextStepVal = original_grid[i][j]
            if nextStepVal == -1:
                continue
            if nextStepVal == 2 and walkable_count - 1 != len(curPath):
                continue 
            nextSteps.append((i, j))

        for i, j in nextSteps:
            newPath = deepcopy(curPath)
            newPath.append((i, j))
            newPathSet = deepcopy(curPathSet)
            newPathSet.add((i, j))

            self.dfs(walkable_count, newPath, newPathSet, original_grid, resultPaths)




        
