class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # print("Mat")
        # for row in mat:
        #     print(row)
        sums = [[0] * len(mat[0]) for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == 0 and j == 0:
                    sums[i][j] = mat[i][j]
                elif i == 0:
                    sums[i][j] = sums[i][j - 1] + mat[i][j]
                elif j == 0:
                    sums[i][j] = sums[i - 1][j] + mat[i][j]
                else:
                    sums[i][j] = sums[i][j - 1] + sums[i - 1][j] - sums[i - 1][j - 1] + mat[i][j]
        # print("Sums")
        # for row in sums:
        #     print(sums)
        answers = [[0] * len(mat[0]) for i in range(len(mat))]
        for i in range(len(answers)):
            for j in range(len(answers[0])):
                upperRow = None if i - k - 1 < 0 else i - k - 1
                lowerRow = len(answers) - 1 if i + k >= len(answers) else i + k
                leftColumn = None if j - k - 1 < 0 else j - k - 1
                rightColumn = len(answers[0]) - 1 if j + k >= len(answers[0]) else j + k
                answerVal = sums[lowerRow][rightColumn]
                if upperRow is not None:
                    answerVal -= sums[upperRow][rightColumn]
                if leftColumn is not None:
                    answerVal -= sums[lowerRow][leftColumn]
                if upperRow is not None and leftColumn is not None:
                    answerVal += sums[upperRow][leftColumn]
                answers[i][j] = answerVal
        # print("Answers")
        # for row in answers:
        #     print(answers)
        return answers
