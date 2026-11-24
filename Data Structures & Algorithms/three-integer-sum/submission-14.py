class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # test cases to consider: [0,0,0,0,0,0,0]
        # [-4,-1,-1,0,1,2]
        nums.sort()
        res = []
        for i in range(len(nums)-2):

            l,r = i+1, len(nums) -1
            if i > 0 and nums[i-1] == nums[i]:
                continue
            while l <r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif total > 0:
                    r -=1
                else:
                    l += 1      
        return res