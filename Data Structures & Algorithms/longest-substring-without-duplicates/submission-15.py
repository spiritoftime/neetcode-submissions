class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        substr = set()
        start = 0
        for i in range(len(s)):
            curr = s[i]
            while curr in substr:
                substr.remove(s[start])
                start += 1
            substr.add(curr)
            res = max(len(substr), res)
        return res
        