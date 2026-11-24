class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def dfs(i, j):
            if (i, j) in cache: return cache[(i, j)]
            if i >= len(word1): return len(word2) - j
            if j >= len(word2): return len(word1) - i
            if word1[i] == word2[j]:
                result = dfs(i+1, j+1)
            else:
                insert  = dfs(i, j+1)
                delete  = dfs(i+1, j)
                replace = dfs(i+1, j+1)
                result  = 1 + min(insert, delete, replace)
            cache[(i, j)] = result
            return result
        return dfs(0, 0)