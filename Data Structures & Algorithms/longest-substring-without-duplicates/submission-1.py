class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        maxLen = 0
        for i in range(len(s)):
            if s[i] in substr:
                substr = substr[substr.index(s[i])+1:]
                substr += s[i]
            else:
                substr += (s[i])
                maxLen = max(maxLen, len(substr))
        return maxLen
        