class Solution:
    def rob(self, nums: List[int]) -> int:
        # at every house, we just want the latest computed result and the one before it
        near,far = 0,0
        for n in nums:
            tmp = max(far + n, near)
            far = near
            near = tmp
        return max(far,near)