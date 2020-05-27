import math
from typing import List

class Solution:
# Solution # 1
    def countNegatives(self, grid: List[List[int]]) -> int:
# [[4,3,2,-1],
# [3,2,1,-1],
# [1,1,-1,-2],
# [-1,-1,-2,-3]]
        count = 0
        height = len(grid)
        width = len(grid[0])
        i = height - 1
        j = 0

# Start from bottom left corner from left to right, iterate until we have found a neg number
        while True:
        # while i >= 0 and j < width:
# if we have found a neg num, all nums after it must be negative also, so add to ccount and move to next row, starting from same col position
            if grid[i][j] < 0:
                count += width - j
                i -= 1
            else:
                j += 1

            if i < 0 or j >= width:
                break
        return count

# Solution 2
    def countNegativesBinSearch(self, grid: List[List[int]]) -> int:
# [[4,3,2,-1],
# [3,2,1,-1],
# [1,1,-1,-2],
# [-1,-1,-2,-3]]

# Solution 2, binary search
#     Starting from bottom row to top:
#         Bin search to get pos of leftmost neg number
#            count += width_of_row - result_of_bin_search
#         For all following row, bin search on range of prev result to end, getting first instance of neg number
        count = 0
        width = len(grid[0])
        i = len(grid) - 1 # height
        j = width - 1
        first_neg_idx = 0

        while i >= 0:
# First check if there are even any negative values in this row, if none, move to the next row
            if grid[i][-1] >= 0:
                i -= 1
                continue

            first_neg_idx = self.find_first_neg_num(grid[i], first_neg_idx, j)
            count += width - first_neg_idx
            i -= 1

        return count


#
    def find_first_neg_num(self, arr: List[int], start, end) -> int:
#       Base Case
        if start == end:
            return start

#       Get middle idx, rounded down if len is odd
        mid_idx = (start + end) // 2


#       If negative
        if arr[mid_idx] < 0:

#           Is it first neg num?
            if self.is_first_neg_num_in_list(arr, mid_idx):
                return mid_idx

#           if not check the left half
            return self.find_first_neg_num(arr, 0, mid_idx)

        else:
#           else check right half
            return self.find_first_neg_num(arr, mid_idx + 1, end)

    def is_first_neg_num_in_list(self, arr: List[int], idx: int) -> bool:
        return arr[idx] < 0 and arr[idx - 1] > 0