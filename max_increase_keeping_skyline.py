class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        skyline_v, skyline_h = self.compute_skylines(grid)
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                max_growth_allowed = min(skyline_h[i], skyline_v[j])
                result += max_growth_allowed - grid[i][j]

        return result

    def compute_skylines(self, grid):
        skyline_v = []
        skyline_h = []
        for i in range(len(grid)):
            skyline_h.append(max(grid[i]))
            skyline_v.append(max([row[i] for row in grid]))

        return skyline_v, skyline_h