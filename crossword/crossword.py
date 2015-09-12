# /**
#  *
#  * Crossword puzzle represented as two-dimensional array
#  * - char == 0 represents empty space
#  *
#  * Valid if all words in puzzle are connected to each other
#  *
#  */

def DFS(puzzle, visited, x, y, rows, cols):
    # visited[x][y] = True
    visited[x*cols + y] = True
    dfsNum += 1
    
    top, left, bottom, right = 0, 0, 0, 0
    if x > 0:
        # check above
        if puzzle[x-1][y] != 0 and not ((x-1)*cols + y) in visited:
            top = DFS(puzzle, visited, x - 1, y, rows, cols)
    if x < rows - 1:
        # check below
        if puzzle[x+1][y] != 0 and not ((x+1)*cols + y) in visited:
            bottom = DFS(puzzle, visited, x + 1, y, rows, cols)
    if y > 0 :
        # check left
        if puzzle[x][y-1] != 0 and not ((x)*cols + y - 1) in visited:
            left = DFS(puzzle, visited, x, y - 1, rows, cols)
    if y < cols - 1:
        # check right
        if puzzle[x][y+1] != 0 and not ((x)*cols + y + 1) in visited:
            right = DFS(puzzle, visited, x, y + 1, rows, cols)
    return top + bottom + left + right + 1

def isValid(puzzle):
    rows = len(puzzle)
    cols = len(puzzle[0])
    characters = 0
    x = -1
    y = -1
    curRow = 0
    curCol = 0
    for row in puzzle:
        for char in row:
            if char != 0:
                if x == -1 and y == -1:
                    x, y = curRow, curCol
                characters += 1
            curCol += 1
        curRow += 1
    
    visited = {}
    
    dfsNum = DFS(puzzle, visited, x, y, rows, cols)
    
    if dfsNum != characters: return False
    else: return True
    