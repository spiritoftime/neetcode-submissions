# 2:16
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # first pass to find the very last index a character appears
        # maintain some sort of sliding window. as you go through, if you meet
        # new characters, the partition will be up to the max of the 
        # last indexes of characters seen
        lastIndex = {}
        res = []
        for i,c in enumerate(s):
            lastIndex[c] = i
        l,r = 0,0
        furthest = 0
        while r < len(s):
            curr = s[r]
            furthest = max(lastIndex[curr], furthest)
            if furthest == r:
                res.append(r-l+1)
                l,r = r+1,r+1
                continue
            r+=1
        return res