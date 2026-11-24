
def binarySearch(nums: List[int], target: int):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return l


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = []
        for n in nums:
            insert_idx = binarySearch(res, n)
            if insert_idx == len(res):
                res.append(n)
            else:
                res[insert_idx] = n
        return len(res)