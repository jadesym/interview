# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Directions
    # 0 - up
    # 1 - right
    # 2 - down
    # 3 - left
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for i in range(m)]

        curNode = head
        curCoord = (0, 0)
        curDirection = 1
        while curNode is not None:
            row, col = curCoord
            matrix[row][col] = curNode.val

            curCoord, curDirection = self.getNextCoords(curCoord, curDirection, m, n, matrix)
            curNode = curNode.next
        return matrix

    def getNextCoords(self, coords: tuple[int, int], direction: int, m: int, n: int, matrix: List[List[int]]) -> tuple[tuple[int, int], int]:
        row, col = coords
        # up -> right
        if direction == 0:
            upRow = None
            if row - 1 >= 0:
                if matrix[row - 1][col] == -1:
                    upRow = row - 1
            return ((row, col + 1), 1) if upRow is None else ((upRow, col), 0)
        # right -> down
        elif direction == 1:
            rightCol = None
            if col + 1 < n:
                if matrix[row][col + 1] == -1:
                    rightCol = col + 1
            return ((row + 1, col), 2) if rightCol is None else ((row, rightCol), 1)
        # down -> left
        elif direction == 2:
            downRow = None
            if row + 1 < m:
                if matrix[row + 1][col] == -1:
                    downRow = row + 1
            return ((row, col - 1), 3) if downRow is None else ((downRow, col), 2)
        # left -> up
        else:
            leftCol = None
            if col - 1 >= 0:
                if matrix[row][col - 1] == -1:
                    leftCol = col - 1
            return ((row - 1, col), 0) if leftCol is None else ((row, leftCol), 3)
