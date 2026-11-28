class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}

        def dfs(i, canBuy):
            if i >= n:
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            skip = dfs(i + 1, canBuy)
            if canBuy:
                act = dfs(i + 1, False) - prices[i]
            else:
                act = dfs(i + 2, True) + prices[i]

            dp[(i, canBuy)] = max(skip, act)
            return dp[(i, canBuy)]

        return dfs(0, True)