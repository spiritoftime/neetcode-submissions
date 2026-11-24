class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        res = s[0]
        for i in range(len(s)):
            dp[(i,i)] = True
        for offset in range(1,len(s)):
            for start in range(len(s) -offset):
                end = start + offset
                dp[(start,end)] = s[start] == s[end]
                if end - start +1 > 2:
                    dp[(start,end)] = dp[(start+1,end-1)] and dp[(start,end)]
                if dp[(start,end)] and len(res) < end - start + 1:
                    res = s[start:end+1]
        return res
