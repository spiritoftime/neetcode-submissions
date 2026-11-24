class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = {c:s.count(c) for c in s }
        tFreq = {c:t.count(c) for c in t }
        return sFreq == tFreq