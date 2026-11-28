class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # 1 way to make amount 0 using any number of coins
        for c in range(len(coins) + 1):
            dp[c][0] = 1

        for c in range(1, len(coins) + 1):
            coin = coins[c - 1]
            for i in range(1, amount + 1):
                # Exclude the current coin
                dp[c][i] = dp[c - 1][i]

                # Include the current coin if it fits
                if i >= coin:
                    dp[c][i] += dp[c][i - coin]

        return dp[-1][-1]