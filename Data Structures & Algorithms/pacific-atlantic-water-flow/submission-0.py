class Solution:
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r,c,visited,prev):
            d = [(0,1),(0,-1),(1,0),(-1,0)]
            if (r,c) in visited or r >= len(heights) or c >= len(heights[0]) or r<0 or c<0 or heights[r][c] < prev:
                return
            visited.add((r,c))
            for r1,c1 in d:
                dfs(r+r1,c+c1,visited,heights[r][c])
        pac,atl = set(),set()
        res = []
        ROWS,COLS = len(heights),len(heights[0])
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res
        