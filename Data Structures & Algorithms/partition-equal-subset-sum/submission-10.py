class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # not possible to split to two equal subset sums 
        if (total //2) * 2 != total: return False
        target = int(total / 2)
        dp = [False for i in range(target + 1)]
        dp[0] = True
        for n in nums:
            # from target to n:
            for amt in range(len(dp) -1, n -1, -1):
                dp[amt] = dp[amt] or dp[amt - n]
        return dp[-1]