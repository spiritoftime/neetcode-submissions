class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        encountered = set()
        l = 0
        res = 0
        for i, c in enumerate(s):
            while c in encountered:
                encountered.remove(s[l])
                l+= 1
            encountered.add(c)
            res = max(len(encountered),res)
        return res