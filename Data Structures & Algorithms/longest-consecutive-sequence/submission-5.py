class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        hashset = set(nums)
        for n in hashset:
            if n-1 not in hashset:
                curr = n
                currLen = 1
                maxLen = max(maxLen,1)
                while curr + 1 in hashset:
                    currLen +=1
                    curr+= 1
                    maxLen = max(maxLen,currLen)
        return maxLen



        