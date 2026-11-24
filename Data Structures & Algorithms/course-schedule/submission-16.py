class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def detectCycle(n, visited):
            if n in visited:return True
            visited.add(n)
            for neigh in adjList[n]:
                if detectCycle(neigh,visited): return True
            visited.remove(n)
            return False
        adjList={n:[] for n in range(numCourses)}
        for c, p in prerequisites:
            adjList[c].append(p)
        visited = set()
        for i in adjList:
            if detectCycle(i,visited):
                return False
        return True