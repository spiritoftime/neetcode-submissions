class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # uses (coins, amt) as key.
        if amount == 0:
            return 0
        memo = {}
        coins.sort()
        res = float('inf')
        for i in range(amount+1):
            coins_needed = i / coins[0]
            if round(coins_needed) != coins_needed: # cannot form
                memo[(coins[0], i)] = float('inf')
            else:
                memo[(coins[0], i)] = coins_needed

            if i == amount:
                res = min(res,memo[(coins[0], i)])
        for i in  range(1,len(coins)):
            for amt in range(amount+1):
                curr_coin = coins[i]
                # float('inf') means impossible to form a combo.

                memo[(curr_coin, amt)] = min(
                    1 + memo.get( (curr_coin, amt - curr_coin),  # use this coin
                        float('inf') ),
                    memo.get((coins[i-1], amt), float('inf')) # dont use this coin
                )
                if amt == amount:
                    res = min(memo[(curr_coin, amt)], res)
        return -1 if res == float('inf') else int(res)      