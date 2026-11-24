class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, curr):
            if (i,curr) in memo:
                return memo[(i,curr)]
            if i == len(nums):
                memo[(i,curr)] = 1 if curr == target else 0
                return memo[(i,curr)]
            memo[(i,curr)] = 0
            memo[(i,curr)] += dp(i+1, curr - nums[i])
            memo[(i,curr)] += dp(i+1, curr + nums[i])
            return memo[(i,curr)]
        return dp(0,0)