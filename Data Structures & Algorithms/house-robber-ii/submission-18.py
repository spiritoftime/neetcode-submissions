class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:return nums[0]
        def dp(nums):
            far,near = 0,0
            for n in nums:
                far,near = near, max(far + n, near)
            return max(far,near)
        return max(dp(nums[1:]), dp(nums[:-1]))