class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # brute force
        coins.sort()
        dp={}
        def backtrack(i, currAmount):
            if currAmount > amount:
                dp[(i,currAmount)] = 0
                return 0
            if (i,currAmount) in dp:
                return dp[(i,currAmount)]
            if currAmount == amount:
                dp[(i,currAmount)] = 1
                return 1 
            res= 0
            for j in range(i,len(coins)):
                if currAmount + coins[j] > amount:
                    break
                currAmount += coins[j]
                res +=backtrack(j, currAmount)
                currAmount -= coins[j]
            dp[(i,currAmount)] =res
            return res
        return backtrack(0, 0)
