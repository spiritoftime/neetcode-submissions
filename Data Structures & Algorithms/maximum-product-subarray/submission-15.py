class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin = 1
        currMax = 1
        for n in nums:
            currMax,currMin = max(currMin * n, currMax *n, n),min(n, n * currMin,currMax * n)
            res = max(currMax, res)
        return res
