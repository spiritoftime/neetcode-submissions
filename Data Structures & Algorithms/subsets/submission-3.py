class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, state = [], []

        def backtrack(i):
            res.append([n for n in state])
            for j in range(i, len(nums)):
                state.append(nums[j])
                backtrack(j + 1)
                state.pop()

        backtrack(0)
        return res