
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = {i: [] for i in range(numCourses)}
        visited = set()
        added = set()

        def detectCycle(curr, visited):
            if curr in visited:
                return True
            if curr in added:
                return False
            visited.add(curr)
            for neigh in graph[curr]:
                if detectCycle(neigh, visited):
                    return True
            visited.remove(curr)
            added.add(curr)
            res.append(curr)
            return False

        for curr, prereq in prerequisites:
            graph[curr].append(prereq)
        for n in graph:
            if detectCycle(n, visited):
                return []
        return res