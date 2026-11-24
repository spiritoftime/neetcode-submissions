class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # res = [cost[i] for i in range(len(cost))]

        # for i in range(len(cost)-3,-1,-1):
        #     res[i] = res[i] + min(res[i+1], res[i+2])
        # return min(res[0], res[1])
        # O(1) reuse input array
        for i in range(len(cost)-3,-1,-1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])