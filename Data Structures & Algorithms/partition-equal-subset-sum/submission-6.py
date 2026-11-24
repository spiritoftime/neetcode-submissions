class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) /2
        if int(target) != target: return False # odd number, no partition
        subset = []
        currSum = 0
        cache = {}
        def dfs(i, subset, currSum):
            if currSum == target: return True
            if (i,currSum) in cache: return cache[(i,currSum)]
            for j in range(i, len(nums)):
                subset.append(nums[j])
                currSum += nums[j]
                if dfs(j+1, subset, currSum): return True
                subset.pop()
                currSum -= nums[j]
            cache[(i,currSum)] = False
            return False
        return dfs(0, subset, currSum)