class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0
        l, r = 0, 0

        while r < len(nums) - 1:  # stop when we can reach the last index
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l = r + 1
            r = furthest
            jumps += 1

        return jumps
