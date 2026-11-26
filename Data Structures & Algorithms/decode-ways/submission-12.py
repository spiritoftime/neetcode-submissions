class Solution:
    def numDecodings(self, s: str) -> int:
        hm ={}
        def dp(i):
            if i in hm: return hm[i]
            # valid combo
            if i == len(s): return 1
            # invalid index
            if i > len(s): return 0 
            c = s[i]
            #cannot start with zero
            if int(c) ==0: return 0
            hm[i] = dp(i+1)
            if i + 1 < len(s) and int(s[i:i+2]) <= 26: hm[i] += dp(i+2)
            return hm[i]
        return dp(0)