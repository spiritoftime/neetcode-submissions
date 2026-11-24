class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # what if matching sequence is halfway through?
        # text1 = cat
        # text2 = abcdegcat
        memo = {}
        def dp(x,y,text1,text2):
            if (x,y) in memo:
                return memo[(x,y)]
            if x >= len(text1) or y >= len(text2):
                memo[(x,y)] = 0
                return 0
            if text1[x] == text2[y]:
                memo[(x,y)] = 1+dp(x+1,y+1,text1,text2)
            else:
                memo[(x,y)] =max(dp(x,y+1,text1,text2),
                dp(x+1,y,text1,text2))
        
            return memo[(x,y)]
        return dp(0,0,text1,text2)