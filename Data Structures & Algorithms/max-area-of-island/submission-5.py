class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        res = 0
        def dfs(r,c, area):
            if r <0 or c <0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] ==0:return 0
            area += 1
            grid[r][c] = 0
            for i,j in directions:
                area += dfs(r+i, c+j, 0)
            return area
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c,0))
        return res