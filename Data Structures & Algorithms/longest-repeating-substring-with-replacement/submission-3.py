class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        hm = {}
        max_freq = 0
        for i in range(len(s)):
            c = s[i]
            hm[c] = hm.get(c,0) + 1
            max_freq = max(max_freq,hm[c])
            if (i - l +1) - max_freq > k:
                hm[s[l]] -=1
                l += 1
        return (i-l+1)
             

            
        