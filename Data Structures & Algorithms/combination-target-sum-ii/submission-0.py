class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        def backtrack(combo,i, total):
            if total > target:
                return
            if total == target:
                self.res.append(list(combo))
                return
            for n in range(i+1,len(candidates)):
                curr = candidates[n]
                newTotal = curr + total
                if curr == candidates[n-1] and n > i+1:
                    continue
                if newTotal <= target:
                    combo.append(curr)
                    backtrack(combo, n , newTotal)
                    combo.pop()
                else:
                    break
        backtrack([],-1,0)
        return self.res
