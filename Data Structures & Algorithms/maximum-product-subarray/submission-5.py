class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 3 choices: take just the curr, running sum (skip curr), or
        # running sum + curr
        # 
        res = nums[0]
        positive, negative = nums[0],nums[0]
        for i in range(1,len(nums)):
            n = nums[i]
            tmp_p = positive * n
            positive = max(n,tmp_p, negative * n)
            negative = min(negative * n, tmp_p, n)
            res = max(positive, negative, res)
        return res

        