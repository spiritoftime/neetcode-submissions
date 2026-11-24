class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        res = 0
        start = 0
        for i,c in enumerate(s):
            hm[c] = hm.get(c,0) +1
            max_freq = max(hm.values())
            while i - start + 1 - max_freq > k: # shrink window when no more
            # replacements available
                hm[s[start]] -=1
                start +=1 
            res = max(i-start+1, res)
        return res
        