class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
#       Generate matrix
        matrix = self.generate_matrix(n, m)
        odd_vals = 0

#       iterate over indices
        for index in indices:
            row, col = index[0], index[1]
#         for each index, iterate row/col
            odd_vals += self.iterate_row(row, matrix)
            odd_vals += self.iterate_col(col, matrix)



#       iterate through matrix, counting odd vals
        # odd_vals = self.count_odds(matrix, altered_rows, altered_cols)

        return odd_vals

    def count_odds(self, m, rows, cols):
        odd_vals = 0

        for row in m:
            for el in row:
                if el % 2 != 0:
                    odd_vals += 1
        return odd_vals

    def iterate_row(self, r, m):
        odd_vals_change = 0
        row = m[r]
        for i in range(len(row)):
            row[i] += 1
            if self.is_odd(row[i]):
                odd_vals_change += 1
            else:
                odd_vals_change -= 1
        return odd_vals_change

    def iterate_col(self, c, m):
        odd_vals_change = 0
        for row in m:
            row[c] += 1
            if self.is_odd(row[c]):
                odd_vals_change += 1
            else:
                odd_vals_change -= 1
        return odd_vals_change

    def is_odd(self, n):
        return n % 2 != 0

    def generate_matrix(self, n, m):
        return [[0 for _ in range(m)] for _ in range(n)]