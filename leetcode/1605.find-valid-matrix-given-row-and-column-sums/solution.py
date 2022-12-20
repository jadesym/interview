from copy import deepcopy

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rowSumCopy = deepcopy(rowSum)
        colSumCopy = deepcopy(colSum)
        rows = len(rowSum)
        cols = len(colSum)
        matrix = [[0] * cols for i in range(rows)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                value = min(rowSumCopy[i], colSumCopy[j])
                matrix[i][j] = value
                rowSumCopy[i] -= value
                colSumCopy[j] -= value
        # print(matrix)
        return matrix