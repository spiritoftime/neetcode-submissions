class Solution:
    def jump(self, nums: List[int]) -> int:
        # res stores jumps needed to reach end from idx i
        res = [float('inf')] * len(nums)
        res[-1] = 0
        for i in range(len(nums)-1,-1,-1):
            curr_jumps = nums[i]
            for j in range(curr_jumps+1):
                if i+j >= len(nums):
                    break
                res[i] = min(res[i], 1 + res[i+j])
        return res[0]

        