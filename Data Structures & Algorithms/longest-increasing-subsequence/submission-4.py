class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearch(LIS, target):
            l,r = 0,len(LIS) -1
            while l <=r:
                m = (l+r)//2
                if LIS[m] == target: return m
                elif LIS[m] < target: l=m+1
                else:r=m-1
            return l


        res = 1
        LIS = [nums[0]]
        for i in range(len(nums)):
            insert_idx = binarySearch(LIS,nums[i])
            if LIS[-1] < nums[i]: # largest so far
                res += 1
                LIS.append(nums[i])
                continue
            LIS[insert_idx] = nums[i] # reconstruct the LIS
        return res
