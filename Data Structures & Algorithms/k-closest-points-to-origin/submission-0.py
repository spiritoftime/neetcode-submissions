class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in range(len(points)):
            x1,y1 = points[i][0],points[i][1]

            distance =  (((x1 - 0)**2 + (y1 - 0)**2)**0.5)
            points[i] = (distance,[x1,y1])
        heapq.heapify(points)
        for i in range(k):
            dist,point = heapq.heappop(points)
            res.append(point)
        return res

            
        