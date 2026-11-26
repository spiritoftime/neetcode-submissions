class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        far,near = cost[0], cost[1]
        for i in range(2, len(cost)):
            far,near = near, cost[i] + min(far,near)
        return min(far,near)