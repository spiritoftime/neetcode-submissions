class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = float('inf')
        for p in prices:
            if p < buy:buy = p
            # always try to sell everyday
            res = max(res, p - buy)
        return res
