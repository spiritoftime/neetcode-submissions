class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, subset):
            nonlocal res
            res.append(subset)
            for n in range(i, len(nums)):
                backtrack(n + 1, subset + [nums[n]])
        backtrack(0, [])
        return res
