class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1:
                dp[(i,i+1)] = s[i] == s[i+1]
                if dp[(i,i+1)]:
                    res +=1
            dp[(i,i)] = True
            res += 1
        for length in range(2, len(s)):
            for start in range(len(s) - length):
                end = start + length
                dp[(start, end)] = s[start] == s[end] and dp[(start +1, end-1)]
                if dp[(start, end)]:
                    res += 1
        return res