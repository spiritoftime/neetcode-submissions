class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi = -1, len(nums)
        while lo+1< hi:
            m = (lo+hi) //2
            if nums[m] <= target: lo=m
            else:hi = m
        if lo == -1 or nums[lo] != target: return -1
        return lo