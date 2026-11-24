class Solution:
    def rob(self, nums: List[int]) -> int:
        def robI(n):
            far,near=0,0
            for money in n:
                tmp = near
                near = max(money + far,near)
                far=tmp
            return near
        return max(nums[0],robI(nums[:-1]), robI(nums[1:]))
