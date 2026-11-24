class Solution:
    def jump(self, nums: List[int]) -> int:
        window_l, window_r = 0, 0
        furthest = 0
        jumps = 0
        while window_r < len(nums) - 1:
            for reachable_index in range(window_l, window_r + 1):
                furthest = max(furthest, reachable_index + nums[reachable_index])
            window_l = window_r + 1
            window_r = furthest
            jumps += 1

        return jumps
