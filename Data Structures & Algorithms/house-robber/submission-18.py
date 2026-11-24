class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:return nums[0]
        far,near = nums[0], max(nums[0],nums[1])
        for n in range(2,len(nums)):
            tmp = near
            near = max( nums[n] + far, near)
            far = tmp
        return max(far, near)