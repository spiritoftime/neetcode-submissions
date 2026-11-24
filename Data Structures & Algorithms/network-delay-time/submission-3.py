class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ''' min heap based on timetaken to choose which edge to traverse'''
        considerations = [(0,k)]
        source_map = defaultdict(list)
        timeTaken = defaultdict(int)
        for t in times:
            source_map[t[0]].append((t[1],t[2])) # destination and time needed
        while considerations: 
            t, sourceNode = heapq.heappop(considerations)
            if sourceNode in timeTaken and t > timeTaken[sourceNode]:continue
            timeTaken[sourceNode] = t
            for destination, t1 in source_map[sourceNode]:
                heapq.heappush(considerations,(t1+t, destination))
        return max(timeTaken.values()) if len(timeTaken) == n else -1