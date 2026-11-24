class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_non_adj(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            far = nums[0]
            near = max(nums[0], nums[1])
            for i in range(2,len(nums)):
                tmp = near
                near = max(nums[i] + far, near)
                far = tmp
            return near
        return max(rob_non_adj(nums[:-1]), rob_non_adj(nums[1:]))