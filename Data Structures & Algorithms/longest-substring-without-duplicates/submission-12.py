class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        encountered = set()
        l,r = 0,0
        res = 0
        for i, c in enumerate(s):
            while c in encountered:
                encountered.remove(s[l])
                l+= 1
            encountered.add(c)
            r = i
            res = max(r-l+1,res)
        return res