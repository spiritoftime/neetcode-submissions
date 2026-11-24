class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if m + n != len(s3):
            return False

        prev = [False for _ in range(m + 1)]
        prev[-1] = True
        for i in range(n, -1, -1):
            curr = [False for _ in range(m + 1)]
            if i == n:
                curr[m] = True
            for j in range(m, -1, -1):
                if i < n and s1[i] == s3[i + j] and prev[j]:
                    curr[j] = True
                if j < m and s2[j] == s3[i + j] and curr[j + 1]:
                    curr[j] = True
            prev = curr
        return prev[0]