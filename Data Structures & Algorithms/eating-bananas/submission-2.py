class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimisation
        def canComplete(m):
            res = 0
            for n in piles:
                res += math.ceil(n/m)
            return res <= h
        lo,hi = 0, max(piles) +1
        while lo+1 < hi:
            m = (lo+hi) // 2
            if canComplete(m):
                hi =m
            else:lo = m
        return hi