import math
def maximalSquare(matrix):
    rows = len(matrix)
    if rows == 0: return 0
    cols = len(matrix[0])
    newMatrix = []
    for a in range(rows):
        newMatrix.append([0]*cols)
    finalmax = int(matrix[0][0])
    newMatrix[0][0] = finalmax
    for x in range(rows):
        for y in range(cols):
            if x == 0 and y == 0: continue
            if x == 0:
                if matrix[x][y] != '0':
                    newMatrix[x][y] = 1
                    if finalmax < 1:
                        finalmax = 1
            elif y == 0:
                if matrix[x][y] != '0':
                    newMatrix[x][y] = 1
                    if finalmax < 1:
                        finalmax = 1
            else:
                if matrix[x][y] == '1':
                    if newMatrix[x-1][y] == newMatrix[x][y-1]:
                        lastSquare = newMatrix[x-1][y]
                        sqrt = int(math.sqrt(lastSquare))
                        if lastSquare == 0:
                            newMatrix[x][y] = 1
                            if finalmax < 1: finalmax = 1
                        elif matrix[x-sqrt][y-sqrt] == '1':
                            newMatrix[x][y] = (sqrt + 1)**2
                            if finalmax < (sqrt + 1)**2: finalmax = (sqrt + 1)**2
                        else:
                            newMatrix[x][y] = 1
                            if finalmax < 1:
                                finalmax = 1
                    else:
                        asqrt = int(math.sqrt(newMatrix[x-1][y]))
                        bsqrt = int(math.sqrt(newMatrix[x][y-1]))
                        if asqrt - bsqrt == 1 or bsqrt - asqrt == 1:
                            newMatrix[x][y] = max(asqrt**2, bsqrt**2)
                        else:
                            newMatrix[x][y] = min(asqrt**2, bsqrt**2)
    print newMatrix
    return finalmax