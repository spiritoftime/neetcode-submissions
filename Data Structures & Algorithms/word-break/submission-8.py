class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i in dp: return dp[i]
            if i == len(s): return True
            for w in wordDict:
                # can find word
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    # if can form the word
                    if dfs(i + len(w)): return True
            dp[i] = False
            return False
        return dfs(0)