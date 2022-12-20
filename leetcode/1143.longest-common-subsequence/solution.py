class Solution:
    # 
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        one_count = len(text1)
        two_count = len(text2)
        oneTwoMatrix = [[0] * two_count for i in range(one_count)]

        for i in range(one_count):
            for j in range(two_count):
                iChar = text1[i]
                jChar = text2[j]
                if i == 0 and j == 0:
                    if iChar == jChar:
                        oneTwoMatrix[i][j] = 1
                    continue

                if i == 0:
                    if iChar == jChar:
                        oneTwoMatrix[i][j] = 1
                    else: oneTwoMatrix[i][j] = oneTwoMatrix[i][j-1]
                    continue

                if j == 0:
                    if iChar == jChar:
                        oneTwoMatrix[i][j] = 1
                    else: oneTwoMatrix[i][j] = oneTwoMatrix[i - 1][j]
                    continue

                topLeft = oneTwoMatrix[i - 1][j - 1]
                if iChar == jChar: topLeft += 1
                oneTwoMatrix[i][j] = max(topLeft, oneTwoMatrix[i-1][j], oneTwoMatrix[i][j-1])
        # print("x", list(text2))
        # for i in range(len(oneTwoMatrix)):
        #     row = oneTwoMatrix[i]
        #     print(text1[i], row)
        return oneTwoMatrix[one_count - 1][two_count - 1]





    