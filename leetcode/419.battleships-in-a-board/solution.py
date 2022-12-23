class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        coordinate_set = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X": coordinate_set.add((i, j))

        visited_set = set()
        ships = 0
        for coord in coordinate_set:
            if coord in visited_set: continue
            ships += 1
            self.dfs(board, coord, coordinate_set, visited_set)            
        return ships

    
    def dfs(self, board: List[List[str]], coords: tuple[int, int], coordinate_set: Set[tuple[int, int]], visited_set: Set[tuple[int, int]]) -> bool:
        m = len(board)
        n = len(board[0])

        queue = [coords]
        while len(queue) > 0:
            coord = queue.pop()
            if coord in visited_set:
                continue
            x, y = coord

            top = (x - 1, y) if x - 1 >= 0 else None
            left = (x, y - 1) if y - 1 >= 0 else None
            bot = (x + 1, y) if x + 1 < m else None
            right = (x, y + 1) if y + 1 < n else None

            if top is not None and top in coordinate_set: queue.append(top)
            if left is not None and left in coordinate_set: queue.append(left)
            if bot is not None and bot in coordinate_set: queue.append(bot)
            if right is not None and right in coordinate_set: queue.append(right)

            visited_set.add(coord)


