class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi = -1, len(nums)
        while lo + 1< hi:
            mid = (lo + hi) //2
            if nums[mid] < target:
                lo = mid
            else: hi = mid
        if hi == len(nums) or nums[hi] != target: return -1
        return hi