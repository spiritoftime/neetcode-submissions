class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #2:13
        # one node can transmit times concurrently!!
        source_map = defaultdict(list)
        shortestTime = float('inf')
        node_time = defaultdict(int)
        for t in times:
            source_map[t[0]].append(t) 
        def dfs(sourceNode, currTime):
            if sourceNode in node_time and currTime > node_time[sourceNode]:
                return
            node_time[sourceNode] = currTime
            for t in source_map[sourceNode]:
                dfs(t[1],currTime + t[2])
        dfs(k,0)
        return max(node_time.values()) if len(node_time) == n else -1