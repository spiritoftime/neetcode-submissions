class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums= [-4,-1,-1,0,1,2]
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                total = nums[i] +nums[l] + nums[r]
                if total >0:
                    r-=1
                elif total < 0:
                    l += 1
                else:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
        return list(list(i) for i in res)