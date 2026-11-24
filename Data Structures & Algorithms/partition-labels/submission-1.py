class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        for i,c in enumerate(s):
            hm[c] = i
        l,r,end =0,0,0
        res = []
        while r<len(s):
            c = s[r]
            end = max(hm[c], end)
            if end == r:
                res.append(r-l+1)
                l = r+1
            r +=1
        return res