class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax,curMin = 1,1
        res = nums[0] # start with nums[0], not 1 or 0 as first num can be neg and len 1
        for n in nums:
            tmp = curMax
            #curMax can be curr num
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp * n, curMin *n, n)
            # because curMax can be just n, you may lose track of optimal soln
            res = max(res,curMax)
        return res