class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_nums = []
#         Get all mins in rows with their indexes
#         check each min to see if it is max in col

        mins = self._get_row_mins(matrix)

        for el in mins:
            num, idx = el
            col = self._get_col(idx, matrix)

            if max(col) == num:
                lucky_nums.append(num)

        return lucky_nums


    def _get_row_mins(self, m):
        mins = []
        for row in m:
            smallest = min(row)
            idx = row.index(smallest)
            mins.append((smallest, idx))

        return mins

    def _get_col(self, idx, m):
        return [row[idx] for row in m]