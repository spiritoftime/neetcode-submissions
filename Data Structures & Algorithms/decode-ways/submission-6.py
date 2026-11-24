class Solution:
    def numDecodings(self, s: str) -> int:
        dp={}
        def dfs(i,dp):
            if i in dp: return dp[i]
            if i == len(s): return 1 # reach the end
            if i > len(s) or s[i] == "0" : return 0

            dp[i] = dfs(i+1,dp)
            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                dp[i] += dfs(i+2,dp)
            return dp[i]
        return dfs(0,dp)
