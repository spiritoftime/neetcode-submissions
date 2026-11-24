class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, curr, combo):
            nonlocal res

            if curr == target:
                res.append(combo.copy())
                return
            if i >= len(candidates) or curr > target:
                return
            for j in range(i, len(candidates)):  # only can use at most once
                if (
                    j > i and candidates[j] == candidates[j - 1]
                ):  # prevent duplicates within the recursion - as long as the next element is same as the previous one, there is opportunity for duplicate. j needs to be less than start before you can compare with the previous element.
                    continue
                newCurr = curr + candidates[j]
                if newCurr > target:
                    break  # no need to continue traversing
                backtrack(j + 1, newCurr, combo + [candidates[j]])
            return

        backtrack(0, 0, [])
        return res