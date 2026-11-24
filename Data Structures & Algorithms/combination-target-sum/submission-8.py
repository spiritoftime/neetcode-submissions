class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(target, i, combo):
            nonlocal res
            if target < 0: return
            if target == 0: 
                res.append(list(combo))
                return
            for j in range(i,len(nums)):
                n = nums[j]
                backtrack(target - n,j, combo + [n])
        backtrack(target,0, [])
        return res