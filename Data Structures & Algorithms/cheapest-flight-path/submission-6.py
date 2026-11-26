import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for s, d, cost in flights:
            graph[s].append((d, cost))

        heap = [(0, src, 0)]          # cost, node, stops
        best_stops = {}               # node -> fewest stops it has been expanded with

        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > k:             # can't take another flight
                continue
            if node in best_stops and best_stops[node] <= stops: # it is not the shortest route
                continue
            best_stops[node] = stops
            for nxt, c2 in graph[node]:
                heapq.heappush(heap, (cost + c2, nxt, stops + 1))
        return -1