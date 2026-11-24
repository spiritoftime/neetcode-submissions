class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''dijistrka and prim's algo differ in the fact that prim's is
        cumulative (minimum spanning tree) whilst dijistrka is shortest path
        (just need the longest of any path)'''
        # build unweighted graph adj list
        adj = defaultdict(list)
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                adj[i].append([cost,j])
                adj[j].append([cost,i])
        minHeap = [[0,0]] # [cost, point]
        visited = set()
        res = 0
        while minHeap:
            cost,point = heapq.heappop(minHeap)
            if point in visited:continue # no need to visit it again
            res += cost
            visited.add(point)
            for c, p in adj[point]:
                heapq.heappush(minHeap,[c, p])
        return res