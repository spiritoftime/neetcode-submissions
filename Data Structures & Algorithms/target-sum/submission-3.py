class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #3:33
        memo = {}
        def dp(i,currSum):
            if (i,currSum) in memo:
                return memo[(i,currSum)]
            if i == len(nums):
                memo[(i,currSum)] = 1 if target==currSum else 0
                return memo[(i,currSum)]
            memo[(i,currSum)] = 0
            curr = nums[i]
            memo[(i,currSum)] += dp(i+1,currSum+curr) + dp(i+1,currSum-curr)
            return memo[(i,currSum)]
        return dp(0,0)
