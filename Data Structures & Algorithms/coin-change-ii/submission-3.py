class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #knapsack
        coins.sort()
        dp = [1] * (amount+1)
        # dp = [[1] * (amount + 1) for _ in range(len(coins))]
        
        for i in range(1,amount+1):
            dp[i] = 1 if i % coins[0] == 0 else 0
        for c in range(1,len(coins)):
            nextDp = [1] * (amount+1)
            for amt in range(amount+1):
                use_coin = nextDp[amt - coins[c]] if amt - coins[c] >= 0 else 0
                nextDp[amt] = use_coin + dp[amt]
            dp = nextDp
        return dp[amount]
        