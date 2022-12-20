class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        skip_mid = m % 2 == 1
        total = 0
        for i in range(m):
            total += mat[i][i]
        for j in range(m):
            total += mat[j][m - j - 1]
        if skip_mid:
            total -= mat[m // 2][m // 2]
        return total

