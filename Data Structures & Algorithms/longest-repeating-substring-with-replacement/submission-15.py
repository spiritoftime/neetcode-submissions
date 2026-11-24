class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        res = 0
        start = 0
        for i in range(len(s)):
            c=s[i]
            hm[c] = hm.get(c,0) + 1
            # if window has more than k replacements
            if (i - start + 1) - max(hm.values()) > k:
                hm[s[start]] -=1
                start +=1
            res = max(i-start+1,res)

        return res


