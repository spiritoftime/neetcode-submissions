class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hm = set(wordDict)  # set is cleaner than {w: True} dict
        cache = {}

        def dfs(i):
            if i == len(s): return True
            if i in cache: return cache[i]

            for j in range(i, len(s)):
                if s[i:j+1] in hm:
                    if dfs(j+1): return True

            cache[i] = False
            return False

        return dfs(0)