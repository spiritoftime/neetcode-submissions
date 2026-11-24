class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob(nums):
            far,near = 0,0
            for i in range(len(nums)):
                tmp = near
                near = max(far + nums[i], near)
                far = tmp
            return near
        # you need to remove one house from each end since you cannot rob first & last
        return max(rob(nums[1:]),
         rob(nums[:-1]))