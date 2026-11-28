class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpable=0
        for i,n in enumerate(nums):
            # can jump here
            if i <= jumpable:
                jumpable = max(jumpable, n + i)
        return jumpable >= len(nums)-1
