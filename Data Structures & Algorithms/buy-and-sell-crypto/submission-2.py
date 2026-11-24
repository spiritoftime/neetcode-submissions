class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,lowest = 0,float('inf')
        for p in prices:
            lowest = min(p,lowest)
            profit = max(profit,p-lowest)
        return profit
