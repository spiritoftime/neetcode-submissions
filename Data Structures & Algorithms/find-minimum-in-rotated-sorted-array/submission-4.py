class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the pivot, minimisation. 
        # find first number that is less than last element
        # condition: m is more than the last element -> not pivot
        lo,hi = -1,len(nums)
        while lo + 1 < hi:
            m = (lo+hi) //2
            if nums[m] <= nums[-1]:
                hi = m
            else: lo = m
        return nums[hi]