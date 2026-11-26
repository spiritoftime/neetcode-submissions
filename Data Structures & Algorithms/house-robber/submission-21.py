class Solution:
    def rob(self, nums: List[int]) -> int:
        # two choices: at nums[i] you rob nums[i-2], or you just rob nums[i-1]
        far,near = 0,0
        for i in range(len(nums)):
            far,near = near, max(far + nums[i], near)
        return max(far,near)