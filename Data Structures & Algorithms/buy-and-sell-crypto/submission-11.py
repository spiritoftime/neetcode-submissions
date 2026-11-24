class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # always try to buy whenever the price is lower
        #always attempt to book profit everyday. this is defined as selling everyday

        buy, sell = float('inf'),float('-inf')
        profit = 0
        for p in prices:
            if p < buy:
                buy = p
                sell = p # if you buy, you need to clear the previous sale price
            if p > sell:
                sell = p
            profit = max(profit, sell- buy)
            
        return profit