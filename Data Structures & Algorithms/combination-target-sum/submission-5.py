class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, state = [], []

        def backtrack(i, curr):
            if curr > target:
                return
            if curr == target:
                res.append([n for n in state])
                return
            for j in range(i, len(candidates)):
                state.append(candidates[j])
                backtrack(j, curr + candidates[j])
                state.pop()

        backtrack(0, 0)
        return res