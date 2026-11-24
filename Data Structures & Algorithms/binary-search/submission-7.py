class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi,lo = len(nums), -1
        while lo+1 < hi:
            m = (lo+hi) //2
            if nums[m] == target: return m
            elif nums[m] > target: 
                hi=m
            else:lo=m
        return hi if hi < len(nums) and nums[hi] == target else -1