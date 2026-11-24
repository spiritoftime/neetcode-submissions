class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low and sell high
        profit = 0
        buy,sell = prices[0],prices[0]
        for p in prices:
            sell = p

            # tally profit every day
            profit = max(profit,sell - buy)
            # if found lower price, should buy on that day. set sell price the same
            # as buy price
            if p < buy:
                buy = p
                sell = p
        return profit