class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        maxLen = 1
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        # (i,j) -> start, end index
        # (i,j) is palindrome if (i+1,j-1) is palindrome and s[i] == s[j].
        # basically a string is palindrome if outer two letters are equal and inside
        # is a palindrome
        for i in range(len(s)): 
            dp[i][i] = True # (i,i) means only one letter so always will be answer
            if i < len(s) -1:
                dp[i][i+1] = s[i] == s[i+1]
                if dp[i][i+1] and maxLen < 2:
                    maxLen = 2
                    res = s[i:i+2]
        for length in range(2, len(s)): # we covered 2 lengths already
            for start in range(len(s) - length):
                end = start + length
                dp[start][end] = s[start] == s[end] and dp[start+1][end-1]
                if dp[start][end] and maxLen < end-start+1:
                    maxLen = end-start+1
                    res = s[start:end+1]
        return res

