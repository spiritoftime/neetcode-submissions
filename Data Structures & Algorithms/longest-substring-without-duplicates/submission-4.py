class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hs = set()
        maxLen = 0
        for i in range(len(s)):
            c = s[i]
            while c in hs:
                hs.remove(s[l])
                l += 1
            hs.add(c)
            maxLen = max(maxLen,len(hs))
        return maxLen
        