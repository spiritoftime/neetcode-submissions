class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """use <= if you want to find an index to insert, even if the target doesnt exist."""
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1

            else:
                l = m + 1
        return l if nums[l] == target else -1