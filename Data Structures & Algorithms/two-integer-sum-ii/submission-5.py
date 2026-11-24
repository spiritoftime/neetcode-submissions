class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hm = {}
        # for i,n in enumerate(numbers):
        #     if n in hm:
        #         return [hm[n],i+1]
        #     hm[target - n] = i+1
        l,r = 0,len(numbers)-1
        while True:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1,r+1]
            elif total < target:
                l +=1
            elif total > target:
                r -=1
            

        
        