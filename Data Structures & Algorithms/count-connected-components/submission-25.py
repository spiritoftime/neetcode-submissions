class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adjList = {i:[] for i in range(n)}    
        for e1,e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
        visited = set()
        def dfs(n):
            visited.add(n)
            for neigh in adjList[n]:
                if neigh not in visited:dfs(neigh)
                
        for i in range(n):
            if i not in visited:
                res +=1
                dfs(i)
        return res