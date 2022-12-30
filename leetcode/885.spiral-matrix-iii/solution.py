class Solution:
    # directions:
    # up = 0
    # right = 1
    # down = 2
    # left = 3

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total_cells = rows * cols
        valid_visited_cells = set()
        visited_cells = set()
        visited_list = []

        curDirection = None
        curCoords = (rStart, cStart)

        while len(valid_visited_cells) < total_cells:
            curCoords, curDirection = self.getNextCoords(rows, cols, curCoords, curDirection, visited_cells, visited_list, valid_visited_cells)
        return visited_list


    def getNextCoords(self, rows: int, cols: int, curCoords: tuple[int, int], direction: Optional[int], visited_cells: Set[tuple[int, int]], visitedList: List[List[int]], valid_visited_cells: Set[tuple[int, int]]) -> tuple[tuple[int, int], int]:
        if self.isValidCell(curCoords, rows, cols):
            valid_visited_cells.add(curCoords)
            visitedList.append(list(curCoords))
        visited_cells.add(curCoords)

        i, j = curCoords

        if direction is None:
            return ((i, j + 1), 1)
        # up
        elif direction == 0:
            if (i, j + 1) not in visited_cells:
                return ((i, j + 1), 1)
            else:
                return ((i - 1, j), 0)
        # right
        elif direction == 1:
            if (i + 1, j) not in visited_cells:
                return ((i + 1, j), 2)
            else:
                return ((i, j + 1), 1)
        # down
        elif direction == 2:
            if (i, j - 1) not in visited_cells:
                return ((i, j - 1), 3)
            else:
                return ((i + 1, j), 2)
        # left
        elif direction == 3:
            if (i - 1, j) not in visited_cells:
                return ((i - 1, j), 0)
            else:
                return ((i, j - 1), 3)



    def isValidCell(self, coords: tuple[int, int], rows: int, cols: int) -> bool:
        i, j = coords
        if i < 0 or i >= rows:
            return False
        if j < 0 or j >= cols:
            return False
        return True