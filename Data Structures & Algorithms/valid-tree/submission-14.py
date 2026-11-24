class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False  # A tree must have exactly n-1 edges
        graph = {i: [] for i in range(n)}
        for e1,e2 in edges:
            graph.get(e1,[]).append(e2)
            graph.get(e2,[]).append(e1)
        
        visited = set()
        def findCycle(curr, prev):
            if curr in visited:
                return True
            visited.add(curr)
            for n in graph[curr]:
                if n == prev:
                    continue
                if findCycle(n,curr):
                    return True
            return False
        if findCycle(0,-1):
            return False

        # Check connectivity
        return len(visited) == n