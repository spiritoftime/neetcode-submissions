class Solution:
    def robI(self,nums):
        far,near = 0,0
        for n in nums:
            tmp = near
            near = max(n+far, near)
            far= tmp
        return near
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.robI(nums[1:]), self.robI(nums[:-1]))
