class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
#       iterate through. ze board
#       if we find an X
#           pass the coords to some other method
#               find and eliminate the ship
        battle_ships = 0

        for y in range(0, len(board)):
            for x in range(0, len(board[0])):
                if board[y][x] == "X":
                    self._sink_battleship(x, y, board)
                    battle_ships += 1

        return battle_ships

    def _sink_battleship(self, x, y, board):
        if y >= len(board) or x >= len(board[0]) or board[y][x] == '.':
            return

        board[y][x] = '.'
        self._sink_battleship(x + 1, y, board)
        self._sink_battleship(x, y + 1, board)