class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        width = len(mat[0])
        height = len(mat)

#       need to traverse height - 1 rows and width - 1 els, top-right and bottom-left corners don't need           sorting


#       ok so we have to traverse width - 1 for row 1
#       then just first el for every other row

#       iterate through first row
        for i in range(0, width - 1):
            diagonal = self._get_diagonal(mat, 0, i, width, height)
            sorted_diagonal = self._sort_diagonal(diagonal)
#           seems weird to mutate original arg but i guess it's alright for sorting?
            mat = self._update_matrix(mat, sorted_diagonal)

#       sort all first el diagonals from row 1 to row height - 1
        for i in range(1, height - 1):
            diagonal = self._get_diagonal(mat, i, 0, width, height)
            sorted_diagonal = self._sort_diagonal(diagonal)
#           seems weird to mutate original arg but i guess it's alright for sorting?
            mat = self._update_matrix(mat, sorted_diagonal)

        return mat

    def _get_diagonal(self, mat, row, col, width, height):
        coords = []
        vals = []
        i = col

        for j in range(row, height):
#           Fail safe condition for Row 0 diagonals that don't span the entire height of matrix
            if i > width - 1:
                break

            vals.append(mat[j][i])
            coords.append((j, i))
            i += 1

        return [vals, coords]

    def _update_matrix(self, mat, diag):
        vals, coords = diag

        for i in range(len(coords)):
            row, col = coords[i]
            val = vals[i]

            mat[row][col] = val

        return mat

    def _sort_diagonal(self, diag):
        vals = sorted(diag[0])
#       sorting by row
        coords = sorted(diag[1], key=lambda x: x[0])

        return [vals, coords]