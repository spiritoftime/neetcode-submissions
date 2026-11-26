class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf') for i in range(amount +1)] for c in coins]
        for i in range(len(coins)): # 0 coins needed to form amount 0
            dp[i][0] = 0
        for i in range(1,amount +1): # do the first coin
            if i >= coins[0]:
                dp[0][i] = 1 + dp[0][i - coins[0]]
        for i in range(1, len(coins)):
            for n in range(1,amount + 1):
                # can we use the current coin?
                if n - coins[i] >= 0:
                    dp[i][n] = min(1 + dp[i][n - coins[i]], dp[i-1][n])
                else:
                    # use the result of the previous coin
                    dp[i][n] = dp[i-1][n]
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1