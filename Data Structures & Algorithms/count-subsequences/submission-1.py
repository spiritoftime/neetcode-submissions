class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(i,j):
            if j >= len(t):return 1
            if i >= len(s):return 0
            if (i,j) in cache: return cache[(i,j)]
            cache[(i,j)] = 0
            for n in range(i, len(s)):
                if s[n] == t[j]:
                    cache[(i,j)] = cache.get((i,j), 0 ) + dfs(n+1, j+1)
            return cache.get((i,j), 0)
        dfs(0,0)
        return cache[(0,0)]
                    