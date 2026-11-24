class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        maxLen = 0
        for i in range(len(s)):
            curr = s[i]
            while curr in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[i])
            maxLen = max(maxLen, len(hashset))
        return maxLen
        