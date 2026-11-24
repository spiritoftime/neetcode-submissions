class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):return False
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:return cache[(i,j)]
            if i == len(s1) and j == len(s2):
                cache[(i,j)] = True
                return cache[(i,j)]
            if i == len(s1): # finished s1, remaining s2 must equal the rest
                cache[(i,j)] = s2[j:] == s3[i+j:]
                return cache[(i,j)]
            if j == len(s2): # finished s2, remaining s1 must equal the rest
                cache[(i,j)] = s1[i:] == s3[i+j:]
                return cache[(i,j)]

            cache[(i,j)] = False
            if s1[i] == s3[i+j]:
                if dfs(i+1,j): return True
            if s2[j] == s3[i+j]:
                if dfs(i,j+1): return True
            return cache[(i,j)]
        return dfs(0,0)
            
