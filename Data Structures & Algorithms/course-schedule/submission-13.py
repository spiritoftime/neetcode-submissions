class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [[0,1],[1,0]]
        graph = {i: [] for i in range(numCourses)}
        visited = set()

        def detectCycle(curr, visited):
            if curr in visited:
                return True
            visited.add(curr)
            for neigh in graph[curr]:
                if detectCycle(neigh, visited):
                    return True
            visited.remove(curr)
            return False  # no cycle

        for curr, prereq in prerequisites:
            graph[curr].append(prereq)
        for c in graph:
            if detectCycle(c, visited):
                return False
        return True