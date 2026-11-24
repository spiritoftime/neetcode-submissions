class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, combo):
            nonlocal res
            if i > len(nums):
                return
            if i <= len(nums):
                res.append(combo.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                backtrack(j + 1, combo + [nums[j]])

        backtrack(0, [])
        return res
