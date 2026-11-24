class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        lowestPrice = float('inf')
        
        for p in prices:
            if p < lowestPrice:
                lowestPrice = p
            else:
                profit = max(p - lowestPrice, profit)
        
        return profit