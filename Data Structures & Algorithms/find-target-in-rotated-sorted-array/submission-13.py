class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(lo, hi):
            # using minimization template
            while lo + 1 < hi:
                m = (lo+hi) //2
                if nums[m] >= target: hi =m
                else: lo = m
            if hi == len(nums) or nums[hi] != target: return -1
            return hi

        # find pivot first (minimum)
        lo,hi = -1, len(nums)
        while lo + 1 <hi:
            m = (lo+hi) //2
            if nums[m]<= nums[-1]:
                hi=m
            else:lo=m
        
        # pivot is at hi.
        if nums[hi] <= target <= nums[-1]: 
            # the lo and the hi must always represent invalid ranges (sentinel)
            # search from pivot to the end
            return binarySearch(hi-1, len(nums))
        else:
            return binarySearch(-1, hi-1)