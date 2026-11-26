class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {n:[] for n in range(n)}
        for e1,e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
        # {
        #     0:[1,2,3],
        #     1:[0,4],
        #     2:[0],
        #     3:[0],
        #     4:[1]
        # }
        #has cycle
        # {
        #     0:[1],
        #     1:[0,2,3,4],
        #     2:[1,3],
        #     3:[2,1],
        #     4:[1]
        # }
        #valid tree: no cycle and all nodes are connected
        visited = set()
        safe = set()
        def isCycle(n,prev):
            if n in visited: return True
            if n in safe: return False
            visited.add(n)
            for neigh in adjList[n]:
                if neigh == prev: continue
                if isCycle(neigh, n): return True

            visited.remove(n)
            safe.add(n)
            return False 
        # shouldnt loop through all, or safe cannot track that all nodes connected 
        if isCycle(0, None):return False
        return True and len(safe) == n