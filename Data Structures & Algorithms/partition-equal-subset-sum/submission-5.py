class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) /2
        if int(target) != target: return False # odd number, no partition
        subset = []
        currSum = 0
        def dfs(i, subset, currSum):
            if currSum == target: return True
            for j in range(i, len(nums)):
                subset.append(nums[i])
                currSum += nums[i]
                if dfs(j+1, subset, currSum): return True
                subset.pop()
                currSum -= nums[i]
            return False
        return dfs(0, subset, currSum)