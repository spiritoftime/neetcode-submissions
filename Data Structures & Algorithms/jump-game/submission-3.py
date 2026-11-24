class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthestAllowedJump =0
        for i in range(len(nums)):
            jumpable = nums[i]
            if i<=furthestAllowedJump:
                furthestAllowedJump = max(furthestAllowedJump, i + jumpable)
        return furthestAllowedJump >= len(nums)-1