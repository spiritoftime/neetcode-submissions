class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i,s):
            if i in memo:
                return memo[i]
            if i > len(s):
                return 0
            if i == len(s):
                memo[i] = 1
                return 1
            if s[i] == '0':
                memo[i]= 0
                return 0
            if int(s[i]) == 1 or int(s[i:i+2]) <= 26: # can dfs twice
                res = dfs(i+1,s) + dfs(i+2,s)
            else:
                res = dfs(i+1,s)
            memo[i] = res
            return res
        return dfs(0,s)
