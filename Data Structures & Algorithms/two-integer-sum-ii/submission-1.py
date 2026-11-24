class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for l in range(len(numbers)):
            if numbers[l] in hm:
                return [hm[numbers[l]]+1,l+1]
            else:
                hm[target - numbers[l]] = l
        
        