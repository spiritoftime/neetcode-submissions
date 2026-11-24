class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i,s):
            if i in memo:
                return memo[i]
            if i > len(s):
                return False
            if i == len(s):
                return True
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    if dfs(i + len(w),s):
                        return True
            memo[i] = False
            return False
        return dfs(0,s)