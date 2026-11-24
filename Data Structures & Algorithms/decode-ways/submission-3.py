class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            if i == len(s): return 1

            if i > len(s) or int(s[i]) == 0: return 0 
            res = dfs(i+1)
            if 9<int(s[i:i+2]) <= 26: res +=dfs(i+2)
            return res
        return dfs(0)