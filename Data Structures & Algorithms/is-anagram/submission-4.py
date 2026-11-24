class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = {}
        tFreq = {}
        for c in s:
            sFreq[c] = sFreq.get(c,0) + 1
        for c in t:
            tFreq[c] = tFreq.get(c,0) + 1    

        return sFreq == tFreq