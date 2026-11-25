class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[(0,1),(0,-1), (1,0), (-1,0)]
        def dfs(i,j):
            area = 1
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]): return 0
            if grid[i][j] == 0:return 0
            grid[i][j] = 0
            for r,c in directions:
                area += dfs(i+r,c+j)
            return area
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(res,dfs(r,c))
        return res