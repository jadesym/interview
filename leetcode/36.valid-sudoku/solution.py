class Solution(object):
    def checkBox(self, left, right, top, bot, board):
        nums = {}
        for x in range(left, right):
            for y in range(top, bot):
                if board[x][y] in nums and board[x][y] != '.': return False
                else: nums[board[x][y]] = True
        return True

    def checkRowOrCol(self, rowOrCol, rowColVal, board):
        nums = {}
        if rowOrCol:
            for x in range(9):
                if board[rowColVal][x] in nums and board[rowColVal][x] != '.': return False
                else: nums[board[rowColVal][x]] = True
        else:
            for y in range(9):
                if board[y][rowColVal] in nums and board[y][rowColVal] != '.': return False
                else: nums[board[y][rowColVal]] = True
        return True
            
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for a in range(0, 7, 3):
            for b in range(0, 7, 3):
                if not self.checkBox(a, a+3, b, b+3, board): return False
        for x in range(9):
            if not self.checkRowOrCol(True, x, board): return False
            if not self.checkRowOrCol(False, x, board): return False
        return True