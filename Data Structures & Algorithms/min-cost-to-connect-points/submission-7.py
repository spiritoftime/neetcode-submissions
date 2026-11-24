class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_cost = [float('inf')] * n # min cost to connect a point to any other point
        res = 0

        # start from first point
        min_cost[0] = 0 # it doesnt cost anything to connect first point since start here
         
        for _ in range(n): # run n times, once per point

            # phase 1 — scan all nodes, find cheapest unvisited node to add to tree
            cheapest_node = -1 # -1 means "havent found a candidate yet"
            for node in range(n):
                if not visited[node] and (cheapest_node == -1 or min_cost[node] < min_cost[cheapest_node]):
                    cheapest_node = node # new cheapest candidate found

            # commit cheapest node to the tree
            res += min_cost[cheapest_node]
            visited[cheapest_node] = True

            # phase 2 — now that cheapest_node joined the tree, check if it offers
            # cheaper connections to any unvisited nodes than what they've seen so far
            # Prim states to always try find cheapest edge, provided edge connects to existing edges
            for neighbor in range(n):
                if not visited[neighbor]: # only update unvisited nodes
                    x1, y1 = points[cheapest_node]
                    x2, y2 = points[neighbor]
                    cost = abs(x1-x2) + abs(y1-y2)
                    if cost < min_cost[neighbor]: # found a cheaper way to reach this neighbor
                        min_cost[neighbor] = cost # update with cheaper cost

        return res