class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) -1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r-=1
                elif total < 0:
                    l+=1
                else:
                    res.add(tuple([nums[i],nums[l],nums[r]]))
                    l+= 1            
        return list(list(i) for i in res)
