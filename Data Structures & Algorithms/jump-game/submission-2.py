class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # start from the back
        # store the lowest successful index able to reach end
        # at every num, if able to jump to lowest successful index
        # update it.
        # at the end if lowest successful = 0, true
        lowest_successful_idx = len(nums) - 1 # last index always can reach
        for i in range(len(nums) -1,-1,-1):
            curr_jumps = nums[i]
            if curr_jumps + i >= lowest_successful_idx:
                lowest_successful_idx = i
        return True if lowest_successful_idx == 0 else False