class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList= {n:[] for n in range(numCourses)}
        visited = set()
        safe = set()
        res = []
        for c,pre in prerequisites:
            adjList[c].append(pre)
        # {
        #     0:[],
        #     1:[0],
        #     2:[]
        # }
        def detectCycle(n):
            if n in visited: return True
            if n in safe: return False
            visited.add(n)
            for neigh in adjList[n]:
                if detectCycle(neigh): return True
            safe.add(n)
            visited.remove(n)
            res.append(n)
            return False


        for n in range(numCourses):
            if detectCycle(n): return []

        return res