class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        squares = 0
        max_square_size = min(len(matrix), len(matrix[0]))

        for i in range(1, max_square_size + 1):
            squares_found = self._square_search(i, matrix)

            if squares_found == 0:
                break

            squares += squares_found

        return squares

    def _square_search(self, square_size: int, m: List[List[int]]) -> int:
        count = 0

        for i in range(0, len(m) - square_size + 1):
            for j in range(0, len(m[0]) - square_size + 1):
                square = self._yank_square(m, i, i + square_size - 1, j, j + square_size - 1)

                if self._is_square_all_ones(square):
                    count += 1

        return count

    def _yank_square(self, m, x1, x2, y1, y2):
        l = []
        for x in range(x1, x2+1):
            l.extend(m[x][y1:y2+1])
        return l

    def _is_square_all_ones(self, l):
        return all(l)