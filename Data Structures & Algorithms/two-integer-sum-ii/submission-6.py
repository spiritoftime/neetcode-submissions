class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarysearch(l, r, target):
            while l <= r:
                m = (l + r) // 2
                if numbers[m] == target: return m
                elif numbers[m] > target: r = m - 1
                else: l = m + 1
            return -1  # not found

        for i in range(len(numbers)):
            complement = target - numbers[i]
            j = binarysearch(i + 1, len(numbers) - 1, complement)
            if j != -1:
                return [i + 1, j + 1]  # 1-indexed