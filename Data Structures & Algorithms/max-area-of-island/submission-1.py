class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            if r <0 or c <0 or r>= len(grid) or c >= len(grid[0]) or grid[r][c] ==0:
                return 0
            grid[r][c] = 0
            area = 1
            for r1,c1 in directions:
                area += dfs(r+r1,c+c1)
            self.res = max(self.res,area)
            return area
        self.res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r,c)
        return self.res
        