class Solution:
    def rob(self, nums: List[int]) -> int:
        near, far = 0,0
        for n in nums:
            tmp = near
            near = max(n + far, near)
            far = tmp
        return near