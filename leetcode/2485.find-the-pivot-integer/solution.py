class Solution:
    def pivotInteger(self, n: int) -> int:
        leftSums = [0] * n
        rightSums = [0] * n
        for i in range(len(leftSums)):
            if i == 0:
                leftSums[i] = i + 1
            else:
                leftSums[i] = leftSums[i-1] + i + 1
        for j in range(len(rightSums) - 1, -1, -1):
            if j == len(rightSums) - 1:
                rightSums[j] = j + 1
            else:
                rightSums[j] = rightSums[j + 1] + j + 1

        # print(leftSums)
        # print(rightSums)

        for i in range(len(leftSums)):
            if leftSums[i] == rightSums[i]:
                return i + 1

        return -1