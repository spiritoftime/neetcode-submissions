class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def backtrack(combo,i,total):
            if total > target:
                return 
            if total == target:
                self.res.append(combo)
                return
            for n in range(i,len(nums)):
                backtrack(combo+ [nums[n]], n, total + nums[n])
        backtrack([],0,0)
        return self.res