class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        def dfs(i,j, prev):
            if i >= len(matrix) or j >= len(matrix[0]) or i <0 or j < 0 or matrix[i][j] <= prev: return 0
            if (i,j) in cache:return cache[(i,j)]
            curr =  matrix[i][j]
            for r,c in directions:
                new_i,new_c =r+i,c+j
                cache[(i,j)] = max(cache.get((i,j), 0), dfs(new_i,new_c, curr) + 1)
            return cache[(i,j)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                 dfs(i,j, float('-inf'))
        return max(cache.values())