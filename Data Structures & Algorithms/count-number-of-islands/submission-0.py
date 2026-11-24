class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0 
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def backtrack(r,c):
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] == "0":
                return 
            curr = grid[r][c]
            grid[r][c] = "0"
            for r1,c1 in directions:
                backtrack(r+r1,c+c1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                curr = grid[r][c]
                if curr == "1":
                    self.res +=1
                    backtrack(r,c)
        return self.res
        