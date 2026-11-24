class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = -1, len(nums)
        while lo + 1 < hi:
            m = (lo + hi) // 2
            if m + 1 < len(nums) and nums[m+1] > nums[m]:
                lo = m   # ascending, peak is to the right
            else:
                hi = m   # descending or edge, peak is here or left
        return hi