class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearch(nums, target):
            lo, hi = -1, len(nums)
            while lo + 1 < hi:
                mid = (lo +hi) // 2
                if nums[mid] > target:
                    hi = mid
                elif nums[mid] == target: return mid
                else:
                    lo = mid
            return hi
        # print(binarySearch([1,3],1))
        # print(binarySearch([1,3],4))

        subsequence = []
        for n in nums:
            if not subsequence or ( subsequence and subsequence[-1] < n): #largest so far
                subsequence.append(n)
                continue
            idx_to_insert = binarySearch(subsequence,n)
            # construct new subsequence
            subsequence[idx_to_insert] = n
        return len(subsequence)
