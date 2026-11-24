class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = 0
        combo = []
        res = []
        l = 0
        while r < len(nums):
            heapq.heappush(combo, (nums[r] * -1, r))  # max heap
            if r - l + 1 == k:
                while l > combo[0][1]:
                    heapq.heappop(combo)
                n = combo[0][0] * -1
                res.append(n)

                l += 1
            r += 1
        return res