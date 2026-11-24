class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:return nums[0]
        res = [nums[i] for i in range(len(nums))]
        for i in range(len(nums)-3,-1,-1):
            res[i] = max(nums[i] + res[i+2], res[i+1])
        return max(res[0], res[1])