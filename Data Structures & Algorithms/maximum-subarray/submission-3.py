class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = [nums[-1]] * len(nums)
        currSum = res[-1]
        for i in range(len(nums)-2,-1,-1):
            res[i] = max(nums[i],nums[i]+currSum)
            currSum = max(nums[i] + currSum, nums[i])
        return max(res)