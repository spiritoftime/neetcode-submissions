from functools import lru_cache
#10:05
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m = len(s1),len(s2)
        if n + m != len(s3):
            return False
        dp = [[False for i in range(m+1)] for j in range(n+1)]
        dp[n][m] = True
        for i in range(n,-1,-1):
            for j in range(m,-1,-1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]

