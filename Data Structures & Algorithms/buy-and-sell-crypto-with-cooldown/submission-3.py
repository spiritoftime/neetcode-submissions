class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1,buy2,sell1 = 0,0,0
        for i in range(len(prices)-1,-1,-1):
            tmp = buy1
            buy1 = max(buy1, sell1 - prices[i])
            sell1 = max(sell1, buy2 + prices[i])
            buy2=tmp
        return buy1