class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        res = 0
        start = 0
        for i in range(len(s)):
            c = s[i]
            
            while c in hm:
                # shrink window
                del hm[s[start]]
                start +=1
            hm[c] = 1
            res = max(len(hm),res)

        return res
                
            

