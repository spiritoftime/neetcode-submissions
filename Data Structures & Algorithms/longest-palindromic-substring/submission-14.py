class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        currLen = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for length in range(len(s)):
            for start in range(len(s) - length):
                end = length + start
                if length <=1:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] =  s[start] == s[end] and dp[start+1][end-1]
                if currLen < end - start +1 and dp[start][end]:
                    res = s[start: end + 1]
                    currLen = end - start +1
        return res
