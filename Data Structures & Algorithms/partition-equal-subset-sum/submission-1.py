class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        memo = {}

        def dp(i, curr_sum):
            """is it possible to form the subset using elements from index i onwards?"""
            if i >= len(nums) or curr_sum < 0:
                memo[(i, curr_sum)] = False
                return False
            if curr_sum == 0:
                memo[(i, curr_sum)] = True

                return True
            include = dp(i + 1, curr_sum - nums[i])
            exclude = dp(i + 1, curr_sum)
            memo[(i, curr_sum)] = include or exclude
            return memo[(i, curr_sum)]

        return dp(0, target)