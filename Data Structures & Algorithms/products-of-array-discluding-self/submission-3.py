class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r =[1 for i in range(len(nums))],[1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i-1]
        for i in range(len(r) - 2, -1,-1):
            r[i] = r[i+1] * nums[i+1]
        out = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            out[i] = r[i] * l[i]
        return out
        