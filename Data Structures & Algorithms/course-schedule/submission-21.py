class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjList = {c: [] for c in range(numCourses)}
        for c, pre in prerequisites:
            adjList[c].append(pre)

        visiting = set()  # nodes in the current DFS path
        safe = set()      # nodes verified to have no cycle

        def hasCycle(n: int) -> bool:
            if n in safe:
                return False
            if n in visiting:
                return True

            visiting.add(n)
            for neigh in adjList[n]:
                if hasCycle(neigh):
                    return True
            visiting.remove(n)
            safe.add(n)
            return False

        for n in range(numCourses):
            if hasCycle(n):
                return False

        return True