class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        dp = [[False for i in range(len(s))] for i in range(len(s)) ]
        for i in range(len(s)):
            dp[i][i] = True
            res += 1
            if i < len(s)-1:
                dp[i][i+1] = s[i] == s[i+1]
                if dp[i][i+1]:            res += 1
        for l in range(2,len(s)):
            for i in range(len(s) - l):
                dp[i][i+l] = s[i] == s[i+l] and dp[i+1][i+l-1]
                if dp[i][i+l]:            res += 1
        return res