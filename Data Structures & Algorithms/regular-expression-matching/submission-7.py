class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        prev = [False] * (len(p)+1)
        prev[len(p)] = True

        for r in range(len(s), -1, -1):
            curr = [False] * (len(p)+1)  # reset each row
            curr[len(p)] = (r == len(s))           # empty pattern matches empty suffix
            for c in range(len(p)-1, -1, -1):
                match = r < len(s) and (p[c] == "." or p[c] == s[r])
                if c+1 < len(p) and p[c+1] == "*":
                    curr[c] = curr[c+2] or (match and prev[c])
                else:
                    curr[c] = match and prev[c+1]
            prev = curr

        return prev[0]

        # dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        # dp[len(s)][len(p)] = True

        # for r in range(len(s), -1, -1):  
        #     for c in range(len(p)-1, -1, -1):
        #         match = r < len(s) and (p[c] == "." or p[c] == s[r])  # guard needed now
        #         if c+1 < len(p) and p[c+1] == "*":
        #             dp[r][c] = dp[r][c+2] or (match and dp[r+1][c])
        #         else:
        #             dp[r][c] = match and dp[r+1][c+1]

        # return dp[0][0]