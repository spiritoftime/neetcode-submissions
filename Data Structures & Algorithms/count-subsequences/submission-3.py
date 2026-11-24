class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev = [0] * (len(t) + 1)
        prev[0] = 1

        for c in s:
            curr = [0] * (len(t) + 1)
            curr[0] = 1
            for i in range(1, len(curr)):
                curr[i] = prev[i]
                if c == t[i-1]:
                    # prev, not curr!
                    curr[i] += prev[i-1]
            prev = curr

        return prev[-1]
            