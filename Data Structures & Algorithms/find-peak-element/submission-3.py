class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def isGreater(i):
            if i == len(nums)-1:return True
            return nums[i] > nums[i+1]
        lo,hi = -1,len(nums)
        while lo +1 < hi:
            m = (lo+hi) //2
            if isGreater(m):hi = m
            else: lo=m
        return hi