rows, cols, rotations = [int(x) for x in input().split()]
oldArray = []
for i in range(rows):
    oldArray.append(input().split())
numLayers = min(rows, cols) // 2
newArray = []
for x in range(rows):
    row = []
    for y in range(cols):
        row.append(oldArray[x][y])
    newArray.append(row)


def printArray(array):
    for row in array:
        print(' '.join(row))

def setNewLoc(nextX, nextY, top, left, right, bottom, rots, origX, origY):
    if rots == 0: return
    x, y = nextX, nextY
    # print("INSIDER SET NEW LOC", nextX, nextY, rots)
    if y == left and x < bottom:
        verticalDiff = bottom - x
        if rots <= verticalDiff:
            newArray[x + rots][y] = oldArray[origX][origY]
        else:
            setNewLoc(x+verticalDiff, y, top, left, right, bottom, rots - verticalDiff, origX, origY)
    elif y == right and x > top:
        verticalDiff = x - top
        if rots <= verticalDiff:
            newArray[x-rots][y] = oldArray[origX][origY]
        else:
            setNewLoc(x-verticalDiff, y, top, left, right, bottom, rots - verticalDiff, origX, origY)
    elif x == top and y > left:
        horizontalDiff = y - left
        if rots <= horizontalDiff:
            newArray[x][y-rots] = oldArray[origX][origY]
        else:
            setNewLoc(x, y - horizontalDiff, top, left, right, bottom, rots - horizontalDiff, origX, origY)
    elif x == bottom and y < right:
    # else:
        horizontalDiff = right - y
        if rots <= horizontalDiff:
            newArray[x][y+rots] = oldArray[origX][origY]
        else:
            setNewLoc(x, y + horizontalDiff, top, left, right, bottom, rots - horizontalDiff, origX, origY)

def rotLayer(pointSet, top, left, right, bottom, rots):
    for point in pointSet:
        nextX, nextY = point
        origX, origY = point
        setNewLoc(nextX, nextY, top, left, right, bottom, rots, origX, origY)
        # print('----', point)
        # printArray(newArray)


for layer in range(numLayers):
    layerCols = cols - layer * 2 - 1
    layerRows = rows - layer * 2 - 1
    numSlots = 2*layerCols + 2*layerRows
    if numSlots == 0: continue
    layerRots = rotations % numSlots
    top = layer
    bottom = rows - layer - 1
    left = layer
    right = cols - layer - 1

    pointSet =  set()
    for xCoord in range(top, bottom + 1):
        pointSet.add((xCoord, left))
        pointSet.add((xCoord, right))
    for yCoord in range(left + 1, right):
        pointSet.add((top, yCoord))
        pointSet.add((bottom, yCoord))
    rotLayer(pointSet, top, left, right, bottom, layerRots)


printArray(newArray)
    