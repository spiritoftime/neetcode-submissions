class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prev = {}
        # 1 way to reach 0
        prev[0] = 1
        # sorta like a bfs
        # only want to keep those that reached target with all the numbers!
        prev = {0: 1}

        for n in nums:
            curr = {}
            for currTotal, ways in prev.items():
                curr[currTotal + n] = curr.get(currTotal + n, 0) + ways
                curr[currTotal - n] = curr.get(currTotal - n, 0) + ways
            prev = curr

        return prev.get(target, 0)
