class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        far, near = cost[0], cost[1] 
        for i in range(2, len(cost)):
            tmp = near
            near = cost[i] + min(far,near)
            far = tmp
        return min(far,near) # both can jump to end