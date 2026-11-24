class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_cost = [float('inf')] * n
        min_cost[0] = 0
        res = 0

        for _ in range(n):
            # linear scan to find cheapest unvisited node
            u = min((i for i in range(n) if i not in visited), key=lambda i: min_cost[i])
            visited.add(u)
            res += min_cost[u]

            x1, y1 = points[u]
            # update min cost to reach each unvisited neighbor
            for v in range(n):
                if v not in visited:
                    x2, y2 = points[v]
                    cost = abs(x1-x2) + abs(y1-y2)
                    min_cost[v] = min(min_cost[v], cost)

        return res