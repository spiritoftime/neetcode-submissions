class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # prev starts from 0 -> 0 ways to form nothing
        prev,curr = [0 for i in range(amount+1)],[0 for i in range(amount+1)]
        for c in coins:
            for i in range(amount+1):
                if i - c >=0:
                    curr[i] = curr[i-c] + prev[i]
                else:
                    if i == 0: 
                        curr[i] = 1 # 1 way to form 0
                    else:
                        curr[i] = prev[i]
            prev = curr
        return curr[amount]
        