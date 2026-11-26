class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        # two choices: at nums[i] you rob nums[i-2], or you just rob nums[i-1]
        far,near = nums[0], max(nums[0],nums[1])
        for i in range(2, len(nums)):
            far,near = near, max(far + nums[i], near)
        return max(far,near)