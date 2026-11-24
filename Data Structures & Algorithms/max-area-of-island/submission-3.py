class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def getMaxArea(i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return (
                1
                + getMaxArea(i + 1, j, grid)
                + getMaxArea(i - 1, j, grid)
                + getMaxArea(i, j + 1, grid)
                + getMaxArea(i, j - 1, grid)
            )

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, getMaxArea(i, j, grid))
        return res
