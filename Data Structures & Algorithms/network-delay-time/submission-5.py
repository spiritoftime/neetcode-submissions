class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        considerations = [(0,k)] #num seconds and node
        source_map = defaultdict(list)
        # how much time it takes to reach node n?
        time_taken = {}
        for source, target, time in times:
            source_map[source].append((time, target))

        while considerations:
            numSeconds, node = heapq.heappop(considerations)
            if node in time_taken and numSeconds > time_taken[node]: # not the shortest path!
                continue
            time_taken[node] = numSeconds
            for t, neighbor in source_map[node]:
                heapq.heappush(considerations, (numSeconds+t, neighbor))
        return max(time_taken.values()) if len(time_taken) == n else -1 # reached all nodes
            