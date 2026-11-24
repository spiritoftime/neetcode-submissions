class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, subset):
            res.append(list(subset))
            for n in range(i, len(nums)):
                if n + 1 <= len(nums):
                    backtrack(n+1, subset + [nums[n]])

        backtrack(0,[])
        return res