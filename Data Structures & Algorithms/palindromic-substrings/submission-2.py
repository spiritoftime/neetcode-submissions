class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}
        res = 0
        for i in range(len(s)):
            dp[(i,i)] = True
            res +=1
        for offset in range(1,len(s)):
            for start in range(len(s) - offset):
                end = start + offset
                dp[(start,end)] = s[start] == s[end]
                if end - start > 1:
                    dp[(start,end)] = dp[(start,end)] and dp[(start+1,end-1)]
                res += 1 if dp[(start,end)] else 0
        return res