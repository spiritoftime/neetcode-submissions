class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        # start from pac and atl cells, then try to flow.
        # tells u can reach pac/ atl
        def dfs(i,j, visited):
            #prevent backtrack for 5 and 5 
            if (i,j) in visited: return 
            curr = heights[i][j]
            # this cell can reach this ocean
            visited.add((i,j))
            # flow from ocean to other cells.
            for x,y in directions:
                if  0<=i+x < len(heights) and 0<= y+j <len(heights[0]) and heights[i+x][y+j] >= curr:
                    dfs(i+x,y+j, visited)
        pac = set()
        atl = set()
        for i in range(len(heights)):
            dfs(i,0,pac)
            dfs(i,len(heights[0])-1, atl)


        for j in range(len(heights[0])):
            dfs(0,j,pac)
            dfs(len(heights)-1,j,atl)


        return list(pac & atl)