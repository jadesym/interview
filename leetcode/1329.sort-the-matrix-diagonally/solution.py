class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        new_mat = [[None] * n for i in range(m)]
        coords_list = [(0, j) for j in range(n)] + [(i, 0) for i in range(1, m)]

        for coords in coords_list:
            sorted_diagonal = self.getDiagonalVals(coords, m, n, mat)
            self.insertDiagonalVals(coords, m, n, sorted_diagonal, new_mat)
        return new_mat


    def getDiagonalVals(self, coords: (int, int), m: int, n: int, mat: List[List[int]]) -> List[int]:
        curX = coords[0]
        curY  = coords[1]
        result = []
        while curX < m and curY < n:
            result.append(mat[curX][curY])
            curX += 1
            curY += 1
        return sorted(result)

    def insertDiagonalVals(self, coords: (int, int), m: int, n: int, diagonal: List[int], new_mat: List[List[int]]) -> None:
        curX, curY = coords
        index = 0
        while curX < m and curY < n:
            new_mat[curX][curY] = diagonal[index]
            curX += 1
            curY += 1
            index += 1
        return
        