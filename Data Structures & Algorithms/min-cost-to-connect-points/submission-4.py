class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # how much it costs to connect to a point of idx i?
        cost_needed = {}
        # start from the first point, connecting it to itself costs nothing.
        # (cost, point_idx) -> you cant do (point_idx, cost) because min heap sorts by first element by default
        considerations = [(0, 0)]
        source_map = defaultdict(list)

        # establish all possible connections
        for i in range(len(points) - 1):
            x1,y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2,y2= points[j][0], points[j][1]
                cost = abs(x1-x2) + abs(y1-y2)
                # store the index so we dont have to store a tuple.
                source_map[i].append((cost,j))
                source_map[j].append(( cost, i))

        while considerations:
            cost,point_idx  = heapq.heappop(considerations)
            # not the min cost
            if point_idx in cost_needed and cost > cost_needed[point_idx]: 
                continue
            cost_needed[point_idx] = cost
            # explore all possible connections at this point
            for  c, p_idx in source_map[point_idx]:
                if p_idx not in cost_needed:
                    heapq.heappush(considerations, (c, p_idx))
        return sum(cost_needed.values()) if len(cost_needed) == len(points) else -1
