class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ls = [[] for i in nums]
        hm = {}
        res=[]
        for num in nums:
            hm[num] = hm.get(num,0) +1
        for num,freq in hm.items():
            ls[freq-1].append(num)
        for i in range(len(ls)-1,-1,-1):
            for num in ls[i]:
                res.append(num)
                if len(res) ==k:
                    return res