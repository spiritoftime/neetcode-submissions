class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi = -1, len(nums)
        while lo+1< hi:
            m = (lo+hi) //2
            if nums[m] >= target: hi=m
            else:lo = m
        if hi == len(nums) or nums[hi] != target: return -1
        return hi