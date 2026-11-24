class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, isBuy):
            if i >= len(prices):
                return 0
            if (i, isBuy) in memo:
                return memo[(i, isBuy)]
            hold = dp(i + 1, isBuy)
            if isBuy:
                buy = dp(i + 1, False) - prices[i]
                memo[(i, isBuy)] = max(buy, hold)
            else:
                sell = dp(i + 2, True) + prices[i]
                memo[(i, isBuy)] = max(hold, sell)

            return memo[(i, isBuy)]

        return dp(0, True)