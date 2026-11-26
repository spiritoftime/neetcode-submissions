class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1 for i in range(n+1)]
        for i in range(2,len(res)):
            res[i] = res[i-1] + res[i-2]
        return res[-1]

