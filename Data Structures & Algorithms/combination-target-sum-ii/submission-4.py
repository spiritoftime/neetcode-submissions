class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, combination, total):
            if total == target: 
                res.append(list(combination))
                return
            if total > target: 
                return 
            for j in range(i, len(candidates)):
                # prevent duplicates within the recursion - 
                # as long as the next element is same as the previous one, 
                # there is opportunity for duplicate. 
                # j needs to be less than start before you can compare with the previous element.
                if j>i and candidates[j] == candidates[j-1]: continue
                if total + candidates[j] > target: continue
                #  advance to the next one
                backtrack(j+1, combination + [candidates[j]], total + candidates[j])
        backtrack(0, [], 0)
        return res