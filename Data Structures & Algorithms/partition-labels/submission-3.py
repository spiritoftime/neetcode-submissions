class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        for i,c in enumerate(s):
            hm[c] = i
        l,end = 0,0
        res = []
        for i,c in enumerate(s):
            end = max(hm[c], end)
            if end == i:
                res.append(i-l+1)
                l=i+1
        


        # while r<len(s):
        #     c = s[r]
        #     end = max(hm[c], end)
        #     if end == r:
        #         res.append(r-l+1)
        #         l = r+1
        #     r +=1
        return res