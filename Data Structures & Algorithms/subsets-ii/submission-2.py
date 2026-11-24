class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, combo):
            if i > len(nums): return
            res.append(list(combo))
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]: continue
                backtrack(j + 1, combo + [nums[j]])
        backtrack(0, [])
        return res