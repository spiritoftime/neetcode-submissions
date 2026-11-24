class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dont count 1 because src -> dst not counted
        # cost, node, numStops
        considerations = [(0, src, 0)]
        source_map = defaultdict(list)
        visited = {}
        for s,d,cost in flights:
            source_map[s].append((cost, d))
        while considerations:
            c, s, numStops = heapq.heappop(considerations)
            if s == dst: return c

            # if s in visited and numStops >=visited[s]: continue # not shortest path
            #because we are using min heap, shortest is the cheapest path
            visited[s] = c
            # while still equal k, can append neighbors
            if numStops <= k:
                for c2, d in source_map[s]:
                    heapq.heappush(considerations, (c+c2, d, numStops + 1)) 
        return -1