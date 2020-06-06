class Solution:
    def judgeCircle(self, moves: str) -> bool:
        movements = {"U": 1, "D": -1, "R": 1, "L": -1}
        vertical_movement = 0
        horizontal_movement = 0

        for move in moves:
            if move == "U" or move == "D":
                vertical_movement += movements[move]
            else:
                horizontal_movement += movements[move]

        return vertical_movement == 0 and horizontal_movement == 0

    def judgeCircleOneLine(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")