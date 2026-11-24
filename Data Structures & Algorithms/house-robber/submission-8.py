class Solution:
    def rob(self, nums: List[int]) -> int:
        # state - at every house to rob or to not rob
        # to decide whether to rob or not rob, should consider which is higher,
        # sum of money earned from prev house or 2 houses away
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        far = nums[0] # 2 houses away
        near = max(nums[0],nums[1]) # 1 house away
        for i in range(2,len(nums)):
            tmp = near
            near = max(far + nums[i], near) 
            far = tmp
        return near
