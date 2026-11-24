class Solution:
    def longestPalindrome(self, s: str) -> str:
        currLen = 1
        res = s[0]
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s) -1:
                dp[i][i+1] = s[i] == s[i+1]
                if dp[i][i+1]:
                    res = s[i:i+2]
                    currLen = 2
        for length in range(2,len(s)):
            for start in range(len(s) - length):
                end = start + length
                dp[start][end] = dp[start+1][end-1] and s[start]==s[end]
                if dp[start][end] and currLen < end-start+1:
                    res = s[start:end+1]
                    currLen = end-start+1
        return res
