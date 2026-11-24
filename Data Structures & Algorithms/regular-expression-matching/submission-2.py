class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i,j):
            if (i,j) in cache: return cache[(i,j)]
            if i >=len(s) and j>=len(p):return True
            if j >= len(p): return False
            match = (i < len(s)) and (p[j] == "." or s[i] == p[j])
            if j +1 < len(p) and p[j+1] == "*":
                skip_curr = dfs(i,j+2)
                repeat_curr = match and dfs(i+1,j)
                cache[(i,j)] = skip_curr or repeat_curr 
            else:
                if match:
                    cache[(i,j)] = dfs(i+1,j+1)
                else: cache[(i,j)] =False
            return cache[(i,j)] 
        return dfs(0,0)
