class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(x,y,n,m):
            if (x,y) in dp:
                return dp[(x,y)]
            if x == n-1 and y == m-1:
                dp[(x,y)] = 1
                return 1
            if x >=n or y >= m:
                dp[(x,y)] = 0
                return 0
            res= dfs(x+1,y,n,m) + dfs(x,y+1,n,m)
            dp[(x,y)] = res
            return res
        return dfs(0,0,n,m)
