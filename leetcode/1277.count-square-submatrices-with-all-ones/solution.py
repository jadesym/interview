class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        square_counts = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    square_counts[i][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    min_square_counts = min(
                        square_counts[i - 1][j], \
                        square_counts[i][j - 1], \
                        square_counts[i - 1][j - 1])
                    square_counts[i][j] = min_square_counts + 1

        result = 0
        for row in square_counts:
            # print(row)
            result += sum(row)
        return result

