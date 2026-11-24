class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i, isBuying):
            if i >= len(prices):return 0
            if (i,isBuying) in cache: return cache[(i,isBuying)]
            hold = dfs(i+1, isBuying)
            if isBuying:
                buy = dfs(i+1, False) - prices[i]
                cache[(i,isBuying)] =max(buy,hold)
            else:
                sell = dfs(i+2, True) + prices[i]
                cache[(i,isBuying)] =max(hold,sell)
            return cache[(i,isBuying)]
        return dfs(0,True)

