class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for i,n in enumerate(numbers):
            if n in hm:
                return [hm[n],i+1]
            hm[target - n] = i+1
        
        