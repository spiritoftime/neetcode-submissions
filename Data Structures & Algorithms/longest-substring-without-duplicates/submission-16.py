class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        substr = set()
        for i in range(len(s)):
            c = s[i]
            while c in substr:
                left = i - len(substr)
                substr.remove(s[left])
            substr.add(c)
            res = max(res, len(substr))
        return res
