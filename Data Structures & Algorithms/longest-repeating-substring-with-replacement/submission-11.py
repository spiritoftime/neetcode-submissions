class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        res = 0
        l = 0
        for i,c in enumerate(s):
            # add the curr letter
            hm[c] = hm.get(c,0) +1
            num_replace = i - l -  max(hm.values())+1

            while num_replace > k:
                hm[s[l]] -= 1
                l+=1
                num_replace = i - l +1- max(hm.values())
            res = max(i-l+1, res)   
        return res