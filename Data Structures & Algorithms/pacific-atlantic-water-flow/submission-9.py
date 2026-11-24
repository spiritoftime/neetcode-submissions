class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start at pac and atl cells, try to perform dfs and flow from them upwards
        # water flows from top to down, so to flow in reverse direction at dfs
        # normal is ocean cell >= neighbor, so opposite is neigh >= ocean cell to flow upward
        # it cannot be more than the next height
        pac,atl = set(), set()
        r,c = len(heights), len(heights[0])
        directions = [(0,1),(0,-1), (1,0), (-1,0)]

        def dfs(i,j,ocean):
            if (i,j) in ocean: return #prevent infinite loop
            ocean.add((i,j))
            for x,y in directions:
                new_r,new_c = i+x, j+y
                if 0<=new_r<r and 0<=new_c<c and  heights[i][j] <=heights[new_r][new_c]:
                    dfs(new_r,new_c,ocean)

        for i in range(r):
            dfs(i,0,pac)
            dfs(i,c-1, atl)

        for j in range(c):
            dfs(0,j,pac)
            dfs(r-1,j,atl)
        return list(pac&atl) # return only cells which appear in both sets


